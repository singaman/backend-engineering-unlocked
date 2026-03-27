import os
import re
import markdown

def final_delivery():
    f_path = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    dist_dir = r"C:\Users\91735\Desktop\Project\notescsv\dist"
    
    # 1. READ AS BINARY AND DECODE SAFELY
    with open(f_path, 'rb') as f:
        data = f.read()
    text = data.decode('utf-8', 'ignore').replace('\r\n', '\n').replace('\r', '\n')
    
    # 2. FILTER OUT GARBAGE (First 1000 lines are problematic)
    lines = text.split('\n')
    clean_lines = []
    found_core = False
    for l in lines:
        if not found_core:
            # Anchor on a known mid-document header
            if '### 1.1 How the Internet Works' in l or '## **Phase 2' in l:
                found_core = True
        
        if found_core:
            if len(l) < 1000 and not any(k in l for k in ['mermaid', 'classDef', 'flowchart', '</div>']):
                clean_lines.append(l)

    core_content = "\n".join(clean_lines)

    # 3. DEFINE ALL 11 PREMIUM DIAGRAMS
    diagrams_html = """
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">🚀 Modern Backend Architecture</h3><pre class="mermaid">
flowchart LR
    Client["📱 Client"]:::client -->|HTTPS| LB{"⚖️ Load Balancer"}:::infra
    LB --> API["🚪 API Gateway"]:::infra
    API <--> Auth["🔐 Auth Service"]:::service
    API --> App["💻 Backend Server"]:::service
    App <--> DB[("🗄️ Database")]:::data
    classDef client fill:#1e293b,stroke:#58a6ff,stroke-width:2px,color:#f0f6fc
    classDef infra fill:#21262d,stroke:#30363d,stroke-width:2px,color:#c9d1d9
    classDef service fill:#0d1117,stroke:#2ea043,stroke-width:2px,color:#f0f6fc
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">🔐 Stateless Auth (JWT) Flow</h3><pre class="mermaid">
sequenceDiagram
    participant User as 👤 User
    participant App as 💻 Server
    User->>App: 1. Login (Credentials)
    App-->>User: 2. Return JWT Token
    User->>App: 3. Request + [JWT]
    App-->>User: 4. Success
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">⚡ Caching Strategy (Cache-Aside)</h3><pre class="mermaid">
sequenceDiagram
    App->>Cache: 1. Get User
    alt Hit
        Cache-->>App: OK
    else Miss
        App->>DB: 2. Query DB
        App->>Cache: 3. Set Cache
    end
</pre></div>
<div class="mermaid-container v-compact"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">🧩 Layered Request Flow</h3><pre class="mermaid">
flowchart LR
    C["📱 Client"] --> H["🎯 Handler"] --> S["🧩 Service"] --> R["🗄️ Repo"] --> D[("📊 DB")]
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">⚙️ Background Task Lifecycle</h3><pre class="mermaid">
sequenceDiagram
    App->>MQ: 1. Push Task
    App-->>Client: 2. 202 Accepted
    MQ->>Worker: 3. Pull Task
    Worker->>Ext: 4. Exec (Email)
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">📡 Scaling: Vertical vs Horizontal</h3><pre class="mermaid">
flowchart TD
    V["🚀 Vertical (Bigger)"]
    H["🏘️ Horizontal (More)"]
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">📦 Microservices Architecture</h3><pre class="mermaid">
flowchart LR
    A[Auth] --- B[Orders] --- C[Payment]
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">🔌 HTTPS TLS 1.3 Handshake</h3><pre class="mermaid">
sequenceDiagram
    C->>S: ClientHello
    S-->>C: ServerHello + Cert
    Note over C,S: Encrypted!
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">💾 Serialization: JSON vs Binary</h3><pre class="mermaid">
flowchart LR
    O[Object] --> J[JSON]
    O --> P[Protobuf]
</pre></div>
<div class="mermaid-container"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">🗄️ Database Types</h3><pre class="mermaid">
flowchart TD
    D[("Databases")] --> R["Relational (SQL)"]
    D --> N["NoSQL (Key-Value/Doc)"]
    D --> G["Graph / Search"]
</pre></div>
<div class="mermaid-container v-compact"><h3 style="text-align: center; color: #58a6ff; margin-bottom:1rem;">📦 The Testing Pyramid</h3><pre class="mermaid">
flowchart TD
    E2E --- Int --- Unit
</pre></div>
"""

    # 4. BUILD HTML
    md = markdown.Markdown(extensions=['toc', 'fenced_code', 'codehilite', 'tables', 'attr_list'])
    html_main = md.convert(core_content)
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Midnight Engineer | Complete Backend Engineering Path & System Design Roadmap</title>
    <meta name="description" content="A 14,000-line masterclass in Backend Engineering. Learn Distributed Systems, Security (Zero Trust/BFF), Observability (OTel), and Modern DevOps from first principles.">
    <meta name="keywords" content="Backend Engineering, System Design, Software Architecture, Distributed Systems, Zero Trust, OpenTelemetry, GitOps, Software Engineer Roadmap">
    <meta name="author" content="Midnight Engineer">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://yourdomain.com/">
    <meta property="og:title" content="Midnight Engineer | Complete Backend Engineering Path">
    <meta property="og:description" content="Master the art of high-scale Backend Systems with this 14,000-line comprehensive curriculum.">
    <meta property="og:image" content="https://yourdomain.com/og-image.png">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://yourdomain.com/">
    <meta property="twitter:title" content="Midnight Engineer | Complete Backend Engineering Path">
    <meta property="twitter:description" content="Master the art of high-scale Backend Systems with this 14,000-line comprehensive curriculum.">
    <meta property="twitter:image" content="https://yourdomain.com/og-image.png">

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    
    <!-- JSON-LD Schema for Google Rich Snippets -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Course",
      "name": "Complete Backend Engineering Path: Midnight Engineer",
      "description": "A comprehensive 14,000-line roadmap from fundamentals to production systems, covering Distributed Systems, Observability, and Zero Trust security.",
      "provider": {{
        "@type": "Organization",
        "name": "Midnight Engineer"
      }}
    }}
    </script>
</head>
<body class="midnight-engineer">
    <div class="layout-container">
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>📚 Curriculum</h2>
            </div>
            <nav id="toc-nav">{md.toc}</nav>
        </aside>
        <main class="content-wrapper">
            <article class="markdown-body">
                <header class="main-header">
                    <h1>Complete Backend Engineering Path</h1>
                    <p>A comprehensive roadmap from fundamentals to production systems.</p>
                </header>
                {diagrams_html}
                <hr style="margin: 3rem 0; border: 0; border-top: 1px solid #30363d;">
                {html_main}
            </article>
        </main>
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            flowchart: {{
                useMaxWidth: false,
                htmlLabels: true,
                curve: 'basis',
                padding: 30
            }},
            sequence: {{
                useMaxWidth: false,
                diagramMarginX: 50,
                diagramMarginY: 10,
                actorMargin: 50,
                width: 150,
                height: 65,
                boxMargin: 10,
                boxTextMargin: 5,
                noteMargin: 10,
                messageMargin: 35
            }},
            themeVariables: {{
                primaryColor: '#161b22',
                primaryTextColor: '#c9d1d9',
                primaryBorderColor: '#58a6ff',
                lineColor: '#58a6ff',
                fontFamily: 'Inter',
                fontSize: '14px',
                clusterBkg: '#0d1117',
                clusterBorder: '#30363d'
            }}
        }});
    </script>
</body>
</html>"""

    with open(os.path.join(dist_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(template)
    print("FINAL SITE DELIVERED SUCCESSFULLY.")

if __name__ == "__main__":
    final_delivery()
