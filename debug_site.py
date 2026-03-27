import os

def debug_md_conversion():
    input_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        md_text = f.read().replace('\r\n', '\n').replace('\r', '\n')
        
    lines = md_text.split('\n')
    processed_lines = []
    mermaid_buffer = []
    state = 0
    
    for line in lines:
        stripped = line.strip()
        if state == 0:
            if stripped.startswith('```mermaid'):
                state = 1
                mermaid_buffer = []
            elif stripped.startswith('```'):
                state = 2
                tag = stripped if stripped != '```' else '```text'
                processed_lines.append(tag)
            else:
                processed_lines.append(line)
        elif state == 1:
            if stripped == '```':
                state = 0
                diagram = '\n'.join(mermaid_buffer)
                processed_lines.append(f'<pre class="mermaid">\n{diagram}\n</pre>')
            else:
                mermaid_buffer.append(line)
        elif state == 2:
            if stripped == '```':
                state = 0
                processed_lines.append(line)
            else:
                processed_lines.append(line)
                
    md_final = '\n'.join(processed_lines)
    
    # Check if md_final contains the corruption 'Client...LB' garble
    with open('md_debug.md', 'w', encoding='utf-8') as f:
        f.write(md_final)
        
    # Search for first mermaid block in md_final
    start = md_final.find('<pre class="mermaid">')
    if start != -1:
        print("Final Markdown Snippet:")
        print("-" * 20)
        print(md_final[start:start+500])
        print("-" * 20)

if __name__ == "__main__":
    debug_md_conversion()
