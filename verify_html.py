import os

def verify_html():
    file_path = r"C:\Users\91735\Desktop\Project\notescsv\dist\index.html"
    if not os.path.exists(file_path):
        print("File not found")
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Look for the first mermaid block
    start_idx = content.find('<pre class="mermaid">')
    if start_idx != -1:
        snippet = content[start_idx:start_idx+500]
        print("Found Mermaid Block:")
        print("-" * 20)
        print(snippet)
        print("-" * 20)
    else:
        print("Mermaid tag not found in HTML")

if __name__ == "__main__":
    verify_html()
