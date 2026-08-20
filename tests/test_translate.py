import subprocess
import os
import sys

def test_translation():
    input_file = "tests/data/input.txt"
    output_file = "tests/data/output.txt"
    
    # Ensure DEEPL_API_KEY is available for the MCP server
    # The MCP server is configured in .ai/mcp/mcp.json and should pick up env vars
    env = os.environ.copy()
    
    # Run translate.py
    cmd = [sys.executable, "tools/translate.py", input_file, output_file]
    
    # Configure stdout to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, encoding='utf-8')
    
    if result.returncode != 0:
        print(f"Translation failed: {result.stderr}")
        return False
        
    with open(output_file, "r", encoding="utf-8") as f:
        output = f.read()
    
    print(f"DEBUG: Output repr: {repr(output)}")
        
    # Verify basic content
    if "Bună, lume" not in output:
        print("Failed: Translation content incorrect")
        return False
        
    # Verify tag preservation
    if '<Listing' not in output or '</Listing>' not in output:
        print("Failed: Tags not preserved or incorrectly translated")
        return False
    
    print("Translation test passed!")
    return True

if __name__ == "__main__":
    if test_translation():
        sys.exit(0)
    else:
        sys.exit(1)
