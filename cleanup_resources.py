import os

def cleanup():
    f_path = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    with open(f_path, 'rb') as f:
        data = f.read()
    
    # Use binary-safe decode
    text = data.decode('utf-8', 'ignore').replace('\r\n', '\n').replace('\r', '\n')
    lines = text.split('\n')
    
    new_lines = []
    skip = False
    for l in lines:
        # Start skip at the header
        if '## **📖 Recommended Resources**' in l:
            skip = True
            continue
        # Stop skip at the next major section (Phase 1 summary)
        if skip and 'Phase 1: Fundamentals' in l:
            skip = False
        
        if not skip:
            new_lines.append(l)

    with open(f_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    print("RESOURCES SECTION REMOVED.")

if __name__ == "__main__":
    cleanup()
