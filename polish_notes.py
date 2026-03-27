import re

def polish_notes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    
    # 1. First Pass: Handle C││ and redundancy
    temp_lines = []
    for line in lines:
        # Fix C││
        line = line.replace('C││', 'C++')
        temp_lines.append(line)

    final_lines = []
    i = 0
    while i < len(temp_lines):
        line = temp_lines[i]
        
        # 2. Remove redundant "text" before code blocks
        # Pattern: "text\n\n```" or "text\n```"
        is_text_only = line.strip() == "text"
        if is_text_only and i + 1 < len(temp_lines):
            next_line = temp_lines[i+1].strip()
            # If next is empty, look one more ahead
            if next_line == "" and i + 2 < len(temp_lines):
                if temp_lines[i+2].strip().startswith("```"):
                    i += 2 # Skip the "text" and the blank line
                    continue
            elif next_line.startswith("```"):
                i += 1 # Skip just the "text" line
                continue
                
        # 3. Handle stray vertical bars
        # A line is stray if it's just whitespace and vertical bars, 
        # and doesn't seem to be part of a multi-line box (not adjacent to border characters).
        strip_line = line.strip()
        if re.fullmatch(r'[│\s]+', strip_line) and len(strip_line.replace(" ", "")) > 0:
            # Check context
            prev_exists = i > 0
            next_exists = i + 1 < len(temp_lines)
            
            p_line = temp_lines[i-1].strip() if prev_exists else ""
            n_line = temp_lines[i+1].strip() if next_exists else ""
            
            # If it's NOT adjacent to box-drawing characters, it's a stray.
            box_chars = set("┌┐└┘├┤┬┴┼─━┃")
            is_part_of_box = any(c in box_chars for c in p_line) or any(c in box_chars for c in n_line)
            
            # Additional check: if it's flanked by empty lines or headers, it's definitely stray.
            is_flanked_by_nothing = (p_line == "" and n_line == "") or n_line.startswith("#")
            
            if not is_part_of_box or is_flanked_by_nothing:
                # Still check if it's meant to be a break between sections.
                # If it's truly isolated, skip it.
                i += 1
                continue

        final_lines.append(temp_lines[i])
        i += 1

    # 4. Box the Recommended Resources section
    # Search for "## **📖 Recommended Resources**"
    for j in range(len(final_lines)):
        if "## **📖 Recommended Resources**" in final_lines[j]:
            # Look for the "Book | Focus" part
            for k in range(j+1, min(j+50, len(final_lines))):
                if "**Book** │ **Focus**" in final_lines[k]:
                    # Build the new box
                    # │  **Book** │ **Focus**                                                           │
                    # │                                                                                 │
                    # │  Designing Data-Intensive Applications │ Database internals, distributed systems    │
                    
                    # I'll just hardcode this specific fix for clarity
                    start_k = k
                    end_k = k
                    # Find where this block ends (usually until next heading or blank block)
                    for m in range(k+1, min(k+20, len(final_lines))):
                        if "###" in final_lines[m] or final_lines[m].strip().startswith("**Node.js**"):
                            end_k = m
                            break
                    
                    if end_k > start_k:
                        resources_box = [
                            "┌─────────────────────────────────────────────────────────────────────────────────────────┐\n",
                            "│  RECOMMENDED BOOKS                                                                      │\n",
                            "├─────────────────────────────────────────────────────────────────────────────────────────┤\n",
                            "│  **Book**                                 │ **Focus**                                   │\n",
                            "├─────────────────────────────────────────────────────────────────────────────────────────┤\n",
                            "│  Designing Data-Intensive Applications    │ Database internals, distributed systems      │\n",
                            "│  Clean Code                               │ Code quality and maintainability            │\n",
                            "│  The Pragmatic Programmer                 │ Software craftsmanship                      │\n",
                            "│  System Design Interview                  │ Interview preparation, real-world architecture│\n",
                            "└─────────────────────────────────────────────────────────────────────────────────────────┘\n"
                        ]
                        # Replace the old lines
                        final_lines[start_k:end_k] = resources_box
                    break
            break

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    polish_notes(target_file)
    print("Polishing complete.")
