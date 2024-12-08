import json
import os
from typing import List, Dict
from src.config import DATA_DIR


class BlogDataLoader:
    @staticmethod
    def load_blog_posts() -> List[Dict]:
        """Load blog posts from JSON file."""
        try:
            json_path = os.path.join(DATA_DIR, "blog_posts.json")

            # Check if file exists
            if not os.path.exists(json_path):
                print(f"File not found at: {json_path}")
                return []

            # Check if file is empty
            if os.path.getsize(json_path) == 0:
                print(f"File is empty: {json_path}")
                return []

            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    print(
                        f"Content read from file: {content[:100]}..."
                    )  # Print first 100 chars for debugging

                    if not content.strip():
                        print("File content is empty")
                        return []

                    data = json.loads(content)

                    if not isinstance(data, dict):
                        print(f"Unexpected data format: {type(data)}")
                        return []

                    if "posts" not in data:
                        print("No 'posts' key in JSON data")
                        return []

                    return data["posts"]

            except json.JSONDecodeError as e:
                print(f"JSON decode error: {str(e)}")
                return []

        except Exception as e:
            print(f"Error in load_blog_posts: {str(e)}")
            return []
