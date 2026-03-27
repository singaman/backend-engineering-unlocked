import re

def create_anchor(text):
    # Remove markdown bolding
    text = text.replace('**', '')
    # Lowercase, replace non-alphanumeric (except spaces/hyphens) with empty, spaces with hyphens
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text

def generate_phase_card(title_match):
    # E.g., title = "Phase 1: Fundamentals (The Foundation)"
    full_title = title_match.group(1).replace('**', '').strip()
    
    parts = full_title.split(':', 1)
    phase_num = parts[0].strip()
    phase_desc = parts[1].strip() if len(parts) > 1 else ""
    
    # 89 width box
    width = 89
    inner_width = width - 4
    
    top = "╔" + "═" * (width - 2) + "╗\n"
    bottom = "╚" + "═" * (width - 2) + "╝\n"
    
    line1 = f"║  {phase_num.upper():<{inner_width}}║\n"
    line2 = f"║  {phase_desc:<{inner_width}}║\n"
    
    card = top + line1 + line2 + bottom
    
    # We still need the actual markdown header for anchors to work in standard markdown
    # But to make it visually pleasing, we'll put the header ABOVE the card, maybe as an HTML anchor or just standard header
    # Standard header makes the TOC work natively in GitHub/VSCode markdown
    # Let's insert the standard header but we'll keep the bold formatting.
    header = f"## **{full_title}**\n\n```\n{card}```\n"
    return header

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    toc_lines = [
        "## **📑 Table of Contents**\n\n",
        "```\n",
        "┌─────────────────────────────────────────────────────────────────────────────────────────┐\n",
        "│  DOCUMENT NAVIGATION                                                                    │\n",
        "└─────────────────────────────────────────────────────────────────────────────────────────┘\n",
        "```\n\n"
    ]
    
    # Step 1: Scan for headers
    # We will look for:
    # Phase headers: ## **Phase 1:
    # Module headers: ### **1.1
    
    for i, line in enumerate(lines):
        phase_match = re.match(r'^##\s+\*\*(Phase\s+\d+.*?)\*\*', line)
        if phase_match:
            title = phase_match.group(1)
            anchor = create_anchor(title)
            toc_lines.append(f"* **[{title}](#{anchor})**\n")
            continue
            
        module_match = re.match(r'^###\s+\*\*(\d+\.\d+\s+.*?)\*\*', line)
        if module_match:
            title = module_match.group(1)
            anchor = create_anchor(title)
            toc_lines.append(f"  * [{title}](#{anchor})\n")

    toc_lines.append("\n---\n\n")

    # Step 2: Insert TOC and replace Phase headers
    new_lines = []
    toc_inserted = False
    
    for i, line in enumerate(lines):
        # Insert TOC right after the initial Curriculum block
        if not toc_inserted and "## **Phase 1: Fundamentals (The Foundation)**" in line:
            new_lines.extend(toc_lines)
            toc_inserted = True
            
        phase_match = re.match(r'^##\s+\*\*(Phase\s+\d+.*?)\*\*', line)
        if phase_match:
            # Generate and insert phase card
            card_block = generate_phase_card(phase_match)
            new_lines.append(card_block)
        else:
            new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    process_file(target_file)
    print("TOC and Phase Cards added.")
