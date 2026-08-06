import google
import genai
from PIL import Image
import json
import os

# ----------------------------
# API KEY
# ----------------------------

API_KEY = os.getenv"GEMINI_API_KEY"

client = genai.Client(api_key=API_KEY)

# ----------------------------
# AI ANALYSIS
# ----------------------------

def analyze_waste(image_path):

    image = Image.open(image_path)

    prompt = """
You are an expert in plastic waste management.

Analyze the uploaded image.

Return ONLY valid JSON.

{
  "plastic_type": "",
  "recyclable": "",
  "quality_score": 0,
  "cleanliness": "",
  "reuse_suggestion": "",
  "environmental_impact": ""
}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            image
        ]
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    try:
        json.loads(text)
        return text

    except Exception:

        return json.dumps({

            "plastic_type": "Unknown",

            "recyclable": "Unknown",

            "quality_score": 50,

            "cleanliness": "Medium",

            "reuse_suggestion": "Reuse whenever possible.",

            "environmental_impact": "Proper recycling helps reduce pollution."

        })

if __name__ == "__main__":
    print("Gemini file loaded successfully")