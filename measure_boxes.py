def measure_boxes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    widths = set()
    for line in lines:
        sline = line.strip()
        if sline.startswith('┌') and sline.endswith('┐'):
            widths.add(len(sline))
        if sline.startswith('╔') and sline.endswith('╗'):
            widths.add(len(sline))
            
    print("Detected box widths:", widths)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    measure_boxes(target_file)
