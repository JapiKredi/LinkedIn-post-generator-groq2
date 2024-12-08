import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Print paths for debugging
print(f"Base Directory: {BASE_DIR}")
print(f"Data Directory: {DATA_DIR}")

# Groq settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY not found in environment variables")

MODEL_NAME = "mixtral-8x7b-32768"

# Generation settings
MODEL_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 500,
    "top_p": 0.95,
}

# Prompt template
BLOG_GENERATION_PROMPT = """Generate a professional LinkedIn blog post about AI technology, following this exact structure:

Your post should be similar in style and depth to this example:

{
    "title": "Breakthrough in AI Development: [Topic]",
    "content": {
        "introduction": "A compelling 2-3 sentence introduction about the main topic",
        "key_points": [
            "First major point with specific details",
            "Second major point with technical insight",
            "Third point about industry impact"
        ],
        "significance": {
            "impact": "Explanation of why this matters to the industry",
            "future": "What this means for future developments"
        },
        "conclusion": "A strong 1-2 sentence wrap-up of the main points and future implications"
    },
    "hashtags": ["#AI", "#Innovation", "#Technology", "#MachineLearning"]
}

Generate the post now:"""
