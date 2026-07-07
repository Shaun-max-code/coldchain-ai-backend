import os

import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Debug information
print("\n========== GEMINI DEBUG ==========")
print("API KEY FOUND :", api_key is not None)

if api_key:
    print("API KEY PREFIX:", api_key[:6] + "...")
    print("API KEY LENGTH:", len(api_key))
else:
    print("API KEY: NOT FOUND")

print("==================================\n")

# Configure Gemini
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_vehicle(vehicle):
    prompt = f"""
You are an AI Cold Chain Logistics Expert.

Analyze the following refrigerated truck.

Vehicle: {vehicle["vehicle"]}
Driver: {vehicle["driver"]}

Temperature: {vehicle["temperature"]} °C
Humidity: {vehicle["humidity"]} %
Speed: {vehicle["speed"]} km/h

Return exactly in this format:

Risk Level:
Problem:
Recommendation:

Keep the response under 100 words.
"""

    try:
        response = model.generate_content(prompt)

        return {
            "vehicle": vehicle["vehicle"],
            "analysis": response.text
        }

    except Exception as e:
        return {
            "vehicle": vehicle["vehicle"],
            "analysis": "Gemini API Error",
            "error": str(e)
        }