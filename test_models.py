import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6K0AIchbUKqHzy07at5E1A0uBWC8jmRD3EqyMP9Ej_1zg")

print("Available Models:\n")

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(model.name)