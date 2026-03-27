import re

def enrich_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the Golden Rules payload for 3.4
    rules_3_4 = """
**Golden Rules for Transactional Emails:**
1. **Never block the main thread**: Always send emails asynchronously via a background queue.
2. **Idempotency is key**: Ensure duplicate webhook events don't result in duplicate emails.
3. **Monitor bounce rates**: High bounce rates can get your domain blacklisted.
"""
    # Insert before the next "###" or "##"
    content = re.sub(
        r'(### \*\*3\.4 Transactional Emails\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + rules_3_4 + "\n",
        content,
        flags=re.DOTALL
    )

    # Define payload for 3.5
    rules_3_5 = """
**Golden Rules for Task Queues:**
1. **Design for failure**: Tasks should be idempotent—safe to rerun if they crash halfway.
2. **Set sensible timeouts**: No task should hang indefinitely and block a worker.
3. **Isolate queues**: Keep critical fast tasks (password resets) on a separate queue from slow batch tasks (report generation).
"""
    content = re.sub(
        r'(### \*\*3\.5 Task Queues & Scheduling\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + rules_3_5 + "\n",
        content,
        flags=re.DOTALL
    )

    # Define payload for 4.8
    rules_4_8 = """
**Golden Rules for Object Storage:**
1. **Never serve large files directly from your application server**: Use signed URLs to let clients upload/download directly to/from S3.
2. **Version your buckets**: Accidental overwrites are common; versioning is an easy safety net.
3. **Set lifecycle policies**: Automatically transition old files to cheaper cold storage to save costs.
"""
    content = re.sub(
        r'(### \*\*4\.8 Object Storage & Large Files\*\*.*?└─────────────────────────────────────────────────────────────────────────────────────────┘\n```.*?)(?=\s*###|\s*##)',
        lambda m: m.group(1) + "\n" + rules_4_8 + "\n",
        content,
        flags=re.DOTALL
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    target_file = r"C:\Users\91735\Desktop\Project\notescsv\Backend_sriniously 3228f0fc161f80c38d60e9d95afae03a.md"
    enrich_content(target_file)
    print("Golden rules added.")
