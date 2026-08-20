import sys
import os
import json
import atexit
from mcp_client import MCPClient

API_KEY = os.environ.get("DEEPL_API_KEY")
if not API_KEY:
    print("Error: DEEPL_API_KEY environment variable not set", file=sys.stderr)
    sys.exit(1)

# Initialize MCP Client
config = json.load(open(".ai/mcp/mcp.json"))
deepl_config = config["mcpServers"]["deepl"]
client = MCPClient(deepl_config["command"], deepl_config["args"], {**os.environ, **deepl_config["env"]})
client.initialize()
client.initialized()
atexit.register(client.close)

def translate(text, target_lang="RO"):
    # Split into paragraphs
    paragraphs = text.split("\n\n")
    translated_paragraphs = []
    
    # Group paragraphs but ensure <Listing> blocks are not split
    chunks = []
    current_chunk = []
    in_listing = False
    
    for p in paragraphs:
        current_chunk.append(p)
        if "<Listing" in p:
            in_listing = True
        if "</Listing>" in p:
            in_listing = False
            
        if not in_listing and len(current_chunk) >= 5:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = []
            
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
        
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            translated_paragraphs.append(chunk)
            continue
            
        print(f"Translating chunk {i+1}/{len(chunks)}...", file=sys.stderr)
        
        # Call MCP server
        response = client.call_tool("translate-text", {
            "text": chunk,
            "targetLangCode": target_lang
        })
        
        if "error" in response:
            print(f"Error: {response['error']}", file=sys.stderr)
            sys.exit(1)
            
        translated = response["result"]["content"][0]["text"]
        
        # Restore escaped tags if HTML handling was used
        translated = translated.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", "\"").replace("&amp;", "&")
        # Fix project-specific tags that DeepL might have translated
        translated = translated.replace("<Listare ", "<Listing ")
        translated = translated.replace("</Listare>", "</Listing>")
        translated = translated.replace(" număr=\"", " number=\"")
        translated = translated.replace(" nume-fișier=\"", " file-name=\"")
        translated = translated.replace(" legendă=\"", " caption=\"")
        
        # Fix common artifacts
        translated = translated.replace("&str;", "&str")
        translated = translated.replace("&text;", "&text")
        
        translated_paragraphs.append(translated)
        
    return "\n\n".join(translated_paragraphs)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", help="Input file")
    parser.add_argument("output", nargs="?", help="Output file")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        import io
        sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
        text = sys.stdin.read()

    if not text.strip():
        sys.exit(0)

    translated = translate(text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(translated)
    else:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        print(translated)
