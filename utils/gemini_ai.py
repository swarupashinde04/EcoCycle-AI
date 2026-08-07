import google.generativeai as genai
from PIL import Image
import json
import os

# ----------------------------
# API KEY
# ----------------------------

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# AI ANALYSIS
# ----------------------------

def analyze_waste(image_path):

    image = Image.open(image_path)

    prompt = """
You are an expert in plastic waste management.

Analyze the uploaded image and return ONLY valid JSON.

{
  "plastic_type": "",
  "recyclable": "",
  "quality_score": 0,
  "cleanliness": "",
  "reuse_suggestion": "",
  "environmental_impact": ""
}
"""

    try:
        response = model.generate_content([prompt, image])

        text = response.text.strip()
        text = text.replace("```json", "").replace("```", "").strip()

        json.loads(text)  # Validate JSON
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
    print("Gemini loaded successfully")
