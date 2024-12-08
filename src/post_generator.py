from src.model import GroqModel
from src.config import BLOG_GENERATION_PROMPT
import json


class PostGenerator:
    def __init__(self):
        self.model = GroqModel()

    def generate_post(self) -> str:
        """Generate a new blog post."""
        try:
            # Generate the content
            generated_text = self.model.generate_completion(BLOG_GENERATION_PROMPT)

            # Try to parse as JSON first
            try:
                # Clean up the text to ensure it's valid JSON
                cleaned_text = self._clean_json_text(generated_text)
                post_data = json.loads(cleaned_text)

                # Format the post in a structured way
                formatted_post = self._format_structured_post(post_data)
            except json.JSONDecodeError:
                # Fallback to text processing if JSON parsing fails
                formatted_post = self._format_unstructured_post(generated_text)

            return formatted_post

        except Exception as e:
            raise Exception(f"Error generating post: {str(e)}")

    def _clean_json_text(self, text: str) -> str:
        """Clean up the generated text to ensure valid JSON."""
        # Find the first '{' and last '}'
        start = text.find("{")
        end = text.rfind("}") + 1
        if start == -1 or end == 0:
            raise ValueError("No valid JSON structure found in generated text")

        return text[start:end]

    def _format_structured_post(self, post_data: dict) -> str:
        """Format a structured post from JSON data."""
        formatted_post = f"""Title: {post_data.get('title', 'New AI Development')}

{post_data.get('content', {}).get('introduction', '')}

Key Points:"""

        # Add key points
        key_points = post_data.get("content", {}).get("key_points", [])
        for point in key_points:
            formatted_post += f"\n• {point}"

        # Add significance
        significance = post_data.get("content", {}).get("significance", {})
        if significance:
            formatted_post += f"\n\nImpact:\n{significance.get('impact', '')}"
            formatted_post += (
                f"\n\nFuture Implications:\n{significance.get('future', '')}"
            )

        # Add conclusion
        conclusion = post_data.get("content", {}).get("conclusion", "")
        if conclusion:
            formatted_post += f"\n\nConclusion:\n{conclusion}"

        # Add hashtags
        hashtags = post_data.get("hashtags", [])
        if hashtags:
            formatted_post += f"\n\n{' '.join(hashtags)}"

        return formatted_post

    def _format_unstructured_post(self, text: str) -> str:
        """Format an unstructured post from raw text."""
        lines = text.split("\n")
        formatted_post = ""
        current_section = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if line.startswith("#"):
                if not formatted_post.endswith("\n\n"):
                    formatted_post += "\n\n"
                formatted_post += line + " "
            elif line.lower().startswith("title:"):
                formatted_post += line + "\n\n"
            else:
                formatted_post += line + "\n"

        return formatted_post.strip()
