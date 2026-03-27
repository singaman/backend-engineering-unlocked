import re

def inject_final_diagrams(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 8. HTTPS Handshake (Phase 1.2)
    https_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Modern HTTPS Handshake (TCP + TLS 1.3)</h3>
```mermaid
sequenceDiagram
    participant Client as 📱 Browser
    participant Server as 💻 Server
    
    rect rgb(22, 27, 34)
    Note over Client, Server: 1. TCP Handshake (3-Way)
    Client->>Server: SYN
    Server-->>Client: SYN-ACK
    Client->>Server: ACK
    end
    
    rect rgb(13, 17, 23)
    Note over Client, Server: 2. TLS 1.3 Handshake (1-Round Trip)
    Client->>Server: ClientHello + Key Share
    Server-->>Client: ServerHello + Certificate + Key Share
    Note over Client, Server: Encrypted channel established!
    end
    
    Client->>Server: GET /index.html (Encrypted)
    Server-->>Client: 200 OK (Encrypted)
```
</div>
"""
    content = re.sub(
        r'(### \*\*1\.2 HTTP Protocol Deep Dive\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + https_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    # 9. Serialization: JSON vs Protobuf (Phase 1.4)
    serial_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">Serialization Formats: Text vs Binary</h3>
```mermaid
flowchart LR
    Data["📦 Application Object<br>{user_id: 123, name: 'Aman'}"]:::data
    
    Data --> JSON["📄 JSON Serialization<br>(Human Readable Text)"]:::json
    Data --> Proto["💾 Protobuf Serialization<br>(Compact Binary)"]:::proto
    
    JSON --> JS[("Larger Size<br>Slow Parsing")]
    Proto --> PS[("Tiny Size<br>Fast Parsing")]

    classDef data fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef json fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#c9d1d9
    classDef proto fill:#161b22,stroke:#d2a8ff,stroke-width:2px,color:#f0f6fc
```
</div>
"""
    content = re.sub(
        r'(### \*\*1\.4 Serialization & Deserialization\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + serial_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    # 10. Database Indexing (Phase 3.1)
    index_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">DB Indexing: B-Tree Visual (Binary Search)</h3>
```mermaid
graph TD
    Root["Root Node (Value 50)"] --> L1["Lower than 50"]
    Root --> R1["Higher than 50"]
    
    L1 --> L1L["10, 20"]
    L1 --> L1R["30, 40"]
    
    R1 --> R1L["60, 70"]
    R1 --> R1R["80, 90"]
    
    style Root fill:#58a6ff,color:#000
    style L1 fill:#1e293b,color:#fff
    style R1 fill:#1e293b,color:#fff
```
</div>
"""
    content = re.sub(
        r'(### \*\*3\.1 Databases\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + index_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    # 11. Testing Pyramid (Phase 5.1)
    pyramid_diagram = """
<div class="mermaid-container">
<h3 style="text-align: center; margin-bottom: 1rem; color: var(--accent);">The Standard Testing Pyramid</h3>
```mermaid
flowchart TD
    E2E["🚀 E2E (Top-Level Flows)<br>Slow, High Cost"]:::e2e
    Int["🧩 Integration (Contract/API)<br>Medium Speed"]:::int
    Unit["📦 Unit (Functions/Logic)<br>Fast, Low Cost"]:::unit
    
    E2E --- Int --- Unit
    
    classDef e2e fill:#1e293b,stroke:#f85149,stroke-width:2px,color:#f0f6fc
    classDef int fill:#161b22,stroke:#f0883e,stroke-width:2px,color:#f0f6fc
    classDef unit fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#f0f6fc
```
</div>
"""
    content = re.sub(
        r'(### \*\*5\.1 Testing\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + pyramid_diagram + "\n",
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    inject_final_diagrams(target_file)
    print("Final expansion complete! Total diagrams: 11.")
