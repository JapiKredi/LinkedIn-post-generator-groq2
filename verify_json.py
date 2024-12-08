# verify_json.py
import json
import os


def verify_json_file():
    json_path = os.path.join("data", "blog_posts.json")

    print(f"Checking JSON file at: {json_path}")

    if not os.path.exists(json_path):
        print("Error: JSON file not found!")
        return

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("File content length:", len(content))
            data = json.loads(content)
            print("JSON structure:", json.dumps(data, indent=2)[:200] + "...")
            print("Verification successful!")
    except Exception as e:
        print(f"Error verifying JSON: {str(e)}")


if __name__ == "__main__":
    verify_json_file()
