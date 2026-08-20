import os
import subprocess
import sys

def batch_translate(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md") and not file.endswith(".ro.md"):
                input_path = os.path.join(root, file)
                # Create the target file name with .ro.md extension
                base_name = os.path.splitext(file)[0]
                output_path = os.path.join(root, base_name + ".ro.md")

                # Skip if translated file already exists
                if os.path.exists(output_path):
                    print(f"Skipping {file}, {output_path} already exists.")
                    continue

                print(f"Translating {input_path} to {output_path}...")
                
                # Call translate.py
                cmd = [sys.executable, "tools/translate.py", input_path, output_path]
                result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
                
                if result.returncode != 0:
                    print(f"Failed to translate {file}: {result.stderr}")
                else:
                    print(f"Successfully translated {file}.")

if __name__ == "__main__":
    src_dir = sys.argv[1] if len(sys.argv) > 1 else "src"
    if os.path.exists(src_dir):
        batch_translate(src_dir)
    else:
        print(f"Directory {src_dir} not found.")
        sys.exit(1)
