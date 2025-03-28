import os

notebook_dir = os.path.dirname(os.path.abspath(".env"))
print(notebook_dir)

with open(".env", "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip() or line.startswith("#"):
            continue

        key, value = line.strip().split("=", 1)
        os.environ[key] = value
