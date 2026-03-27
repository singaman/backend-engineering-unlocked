import re

def inject_auth_diagram(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. Authentication Diagram (Stateless/JWT)
    auth_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Modern Stateless Auth (JWT) Flow</h3>
```mermaid
sequenceDiagram
    participant User as 👤 User
    participant App as 💻 Server
    participant DB as 🗄️ Database

    User->>App: 1. Login (Username/Password)
    App->>DB: 2. Verify Credentials
    DB-->>App: OK
    Note right of App: Generate JWT (Signed)
    App-->>User: 3. Return JWT (Token)
    Note over User, App: Future Requests include JWT Header
    User->>App: 4. Request Data + [JWT]
    App->>App: 5. Verify Signature (No DB lookup!)
    App-->>User: 6. Return Data
```
</div>
"""
    
    # Insert after "### **2.1 Authentication & Authorization**"
    content = re.sub(
        r'(### \*\*2\.1 Authentication & Authorization\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + auth_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    inject_auth_diagram(target_file)
    print("Auth diagram injected!")
