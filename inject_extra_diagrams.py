import re

def inject_extra_diagrams(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Caching Strategy Diagram (Cache-Aside)
    caching_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">The Cache-Aside Pattern</h3>
```mermaid
sequenceDiagram
    participant App as 💻 Backend App
    participant Cache as ⚡ Redis (Cache)
    participant DB as 🗄️ PostgreSQL (DB)

    App->>Cache: 1. Check for data (GET key)
    alt Cache Hit
        Cache-->>App: Return data
    else Cache Miss
        Cache-->>App: Not found
        App->>DB: 2. Query Database
        DB-->>App: Return result
        App->>Cache: 3. Store result (SET key)
        App-->>App: Continue processing
    end
```
</div>
"""
    
    # Insert after "### **3.3 Caching**"
    content = re.sub(
        r'(### \*\*3\.3 Caching\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + caching_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    # 2. Database Scaling Diagram
    scaling_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Horizontal vs Vertical Scaling</h3>
```mermaid
flowchart TD
    subgraph Vertical ["🚀 Vertical Scaling (Scaling Up)"]
        V1["Small Server<br>(2 vCPU, 4GB)"] --> V2["Large Server<br>(64 vCPU, 256GB)"]
    end
    
    subgraph Horizontal ["🏗️ Horizontal Scaling (Scaling Out)"]
        H1["Server 1"] --- H2["Server 2"] --- H3["Server 3"] --- H4["Server N"]
        LB["Balancing Traffic..."] --> H1 & H2 & H3 & H4
    end

    classDef vertical fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef horizontal fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#f0f6fc
```
</div>
"""
    # Insert after "### **4.6 Scaling & Performance**"
    content = re.sub(
        r'(### \*\*4\.6 Scaling & Performance\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + scaling_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    inject_extra_diagrams(target_file)
    print("Extra diagrams injected!")
