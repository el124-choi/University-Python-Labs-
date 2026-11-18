from pathlib import Path 

def atomic_write(target_path: Path, data: list[str]):
    with open(target_path, "w") as f: 
        for line in data: 
            f.write(f"{line}\n") # Write each line followed by a newline character

data = [
    "2026-10-12 14:00:01 192.168.1.10 GET /index.html 200 INFO Request_successful ",

    "2026-10-12 14:00:02 192.168.1.11 POST /api/v1/login 200 INFO Authenticated_user",

    "2026-10-12 14:00:03 192.168.1.12 GET /api/v1/checkout 500 ERROR Connection_failed",

    "2026-10-12 14:00:04 192.168.1.13 GET /images/logo.png 304 INFO Resource_not_modified ",

    "2026-10-12 14:00:05 192.168.1.14 POST /api/v1/pay 503 ERROR Gateway_timeout_upstream",

    "2026-10-12 14:00:06 192.168.1.15 DELETE /api/v1/user/42 403 ERROR Permission_denied",

    "2026-10-12 14:00:07 192.168.1.16 GET /static/css/main.css 200 INFO Asset_served",

    "2026-10-12 14:00:08 192.168.1.17 GET /api/v1/products 200 INFO Query_returned_20_items ",

    "2026-10-12 14:00:09 192.168.1.18 POST /api/v1/upload 413 ERROR Payload_too_large",
]

path = Path("data.txt") 

atomic_write(path, data)