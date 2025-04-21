from google import genai
from google.genai import types
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Configure the API key
client = genai.Client(api_key="YOUR_API_KEY_HERE")

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    # Add specific instructions for MermaidJS format
    enhanced_prompt = f"Generate a MermaidJS diagram for: {prompt}. Return only the MermaidJS code without any explanation, no `s, only start from graph. "
    
    # Use the correct method to generate content
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = enhanced_prompt
        )  
    # Access the generated text and clean it
    mermaid_code = response.text.strip()  # Remove leading/trailing whitespace
    mermaid_code = mermaid_code.replace('`', '')  # Remove backticks
    mermaid_code = mermaid_code.replace('mermaid', '')  # Remove the word "mermaid"
    mermaid_code = "\n".join([line.strip() for line in mermaid_code.splitlines() if line.strip()])  # Remove blank lines
    print(mermaid_code)

    # Return the generated MermaidJS code as JSON
    return jsonify({'mermaid_code': mermaid_code})

if __name__ == '__main__':
    app.run(debug=True)
    
