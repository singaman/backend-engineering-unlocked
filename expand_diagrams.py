import re

def inject_more_diagrams(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 4. Request Flow Diagram (Handler -> Service -> Repo)
    request_flow = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Standard Backend Layered Pattern</h3>
```mermaid
flowchart TD
    Client["📱 Client"] --> Handler["🎯 Handler (Entry Point)<br>Validation & Status Codes"]
    Handler --> Service["🧩 Service Layer<br>Core Business Logic"]
    Service --> Repo["🗄️ Repository Layer<br>Data Access / Raw Queries"]
    Repo --> DB[("📊 PostgreSQL DB")]
    
    classDef main fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef sub fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#c9d1d9
    class Client,Handler main
    class Service sub
    class Repo,DB sub
```
</div>
"""
    
    # Insert after "### **2.5 Handlers & Controllers (CRUD Operations)**"
    content = re.sub(
        r'(### \*\*2\.5 Handlers & Controllers \(CRUD Operations\)\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + request_flow + "\n",
        content,
        flags=re.DOTALL
    )

    # 5. Task Queue Diagram (Phase 3.5)
    queue_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Asynchronous Task Lifecycle</h3>
```mermaid
sequenceDiagram
    participant App as 💻 Main App
    participant Queue as ⚙️ Redis/RabbitMQ (Queue)
    participant Worker as 👷 Background Worker
    participant Ext as 📧 Email/3rd Party

    App->>Queue: 1. Push Task (e.g., Send Email)
    App-->>App: 2. Return 202 Accepted to Client
    Note over Queue, Worker: Task stays in queue until free
    Queue->>Worker: 3. Pull Task
    Worker->>Ext: 4. Execute (e.g. Send Email)
    Worker-->>Queue: 5. Acknowledge Success
```
</div>
"""
    # Insert after "### **3.5 Task Queues & Scheduling**"
    content = re.sub(
        r'(### \*\*3\.5 Task Queues & Scheduling\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + queue_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    # 6. Microservices Diagram (Phase 4.9)
    micro_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Monolith vs Microservices</h3>
```mermaid
flowchart LR
    subgraph Monolith ["💎 Monolith Architecture"]
        M[Everything in one app]
    end
    
    subgraph Micro ["🛰️ Microservices Architecture"]
        A[Auth Service] --- B[Order Service] --- C[Payment Service]
        D[Notification Service] --- B
    end
    
    classDef mon fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef mic fill:#0d1117,stroke:#f0883e,stroke-width:2px,color:#f0f6fc
```
</div>
"""
    # Insert after "### **4.9 Real-time Backend Systems**"
    # Wait, 4.9 is Real-time, but Microservices is often mentioned in Scaling/Systems.
    # Let's find a good spot in Phase 4.
    content = re.sub(
        r'(### \*\*4\.9 Real-time Backend Systems\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + micro_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    inject_more_diagrams(target_file)
    print("All diagrams expanded!")
