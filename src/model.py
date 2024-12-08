from groq import Groq
from src.config import GROQ_API_KEY, MODEL_NAME, MODEL_CONFIG


class GroqModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GroqModel, cls).__new__(cls)
            cls._instance._initialize_client()
        return cls._instance

    def _initialize_client(self):
        """Initialize the Groq client."""
        try:
            self.client = Groq(api_key=GROQ_API_KEY)
            print("Groq client initialized successfully!")
        except Exception as e:
            raise Exception(f"Error initializing Groq client: {str(e)}")

    def generate_completion(self, prompt: str) -> str:
        """Generate completion using Groq API."""
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=MODEL_NAME,
                temperature=MODEL_CONFIG["temperature"],
                max_tokens=MODEL_CONFIG["max_tokens"],
                top_p=MODEL_CONFIG["top_p"],
            )

            return completion.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")
