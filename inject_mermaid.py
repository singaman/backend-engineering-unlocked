import re

def add_mermaid_diagram(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    mermaid_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Modern Backend Architecture: The Big Picture</h3>
```mermaid
flowchart LR
    Client["📱 Client<br>(Browser/App)"]:::client -->|HTTP/HTTPS| LB{"⚖️ Load Balancer"}:::infra
    
    LB --> API["🚪 API Gateway<br>(Routing & Auth)"]:::infra
    
    API <--> Auth["🔐 Auth Service<br>(JWT/OAuth)"]:::service
    API --> App["💻 Backend Server<br>(Business Logic)"]:::service
    
    App <--> Cache[("⚡ Redis Cache<br>(In-Memory)")]:::data
    App <--> DB[("🗄️ PostgreSQL<br>(Relational DB)")]:::data
    App --> Queue{"⚙️ Task Queue<br>(RabbitMQ/Kafka)"}:::queue
    
    Queue --> Worker["👷 Background Worker"]:::service
    Worker <--> S3[("☁️ S3 Bucket<br>(Object Storage)")]:::data
    Worker --> Email["📧 Email Provider"]:::infra
    
    classDef client fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef infra fill:#21262d,stroke:#30363d,stroke-width:2px,color:#c9d1d9
    classDef service fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#f0f6fc
    classDef data fill:#161b22,stroke:#d2a8ff,stroke-width:2px,color:#f0f6fc
    classDef queue fill:#21262d,stroke:#f0883e,stroke-width:2px,color:#f0f6fc
```
</div>
"""
    
    # We want to insert this right after the "BACKEND ENGINEERING ROADMAP" box
    # which is lines 10-15 roughly. Let's find "│  From Fundamentals to Production-Ready Systems                                          │"
    # and "└─────────────────────────────────────┘"
    
    # Insert safely after the first instance of '```text' block that closes
    search_pattern = r"(## \*\*📚 Complete Backend Engineering Curriculum\*\*\n\n```text\n┌.*?\n│.*?\n│.*?\n└.*?\n```\n)"
    content = re.sub(search_pattern, lambda m: m.group(1) + "\n" + mermaid_diagram + "\n", content, count=1, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    add_mermaid_diagram(target_file)
    print("Mermaid diagram injected successfully!")
