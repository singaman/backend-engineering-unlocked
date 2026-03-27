import markdown

def minimal_build():
    content = """
# Test
<div class="mermaid-container">
<pre class="mermaid">
flowchart LR
    A-->B
</pre>
</div>
"""
    md = markdown.Markdown(extensions=['fenced_code', 'codehilite'])
    html = md.convert(content)
    print("HTML Output:")
    print("-" * 20)
    print(html)
    print("-" * 20)

if __name__ == "__main__":
    minimal_build()
