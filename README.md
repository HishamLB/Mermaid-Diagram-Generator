# MermaidJS Diagram Generator

A web-based tool that generates MermaidJS diagrams from text descriptions using AI. Simply describe what you want, and get a rendered MermaidJS diagram instantly.

## 🌟 Features

- Web-based interface
- Real-time diagram generation
- Powered by Google's Gemini AI [adding other models soon]
- Supports all MermaidJS diagram types

## 🛠️ Prerequisites

- Python 3
- Flask
- Google GenerativeAI API key

## 📦 Installation

1. Clone the repository:
```bash
git clone (https://github.com/HishamLB/Mermaid-Diagram-Generator-.git)
cd mermaid-diagram-generator
```

2. Install required Python packages:
```bash
pip install flask google-generativeai
```

3. Set up your Google API key:
   - Get an API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Replace the API key in `app.py` with your key:
```python
client = genai.Client(api_key="YOUR_API_KEY_HERE")
```

## 🚀 Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## 💡 How to Use

1. Enter your diagram description in the text area
2. Click "Generate Diagram"
3. View your generated MermaidJS diagram

### Example Input:
```
Create a flowchart showing user login process
```

## 📚 MermaidJS Resources

- [Official MermaidJS Documentation](https://mermaid.js.org/)
- [MermaidJS Live Editor](https://mermaid.live/)
- [MermaidJS Syntax Guide](https://mermaid.js.org/syntax/flowchart.html)

## 🔧 Supported Diagram Types

- Flowcharts
- Sequence diagrams
- Class diagrams
- State diagrams
- Entity Relationship diagrams
- User Journey diagrams
- Gantt charts
- Pie charts
- And more!

## 🤝 Contributing

You are free to do anything with the source code 

## ⚠️ Security Note

Never commit API keys to version control. Consider using environment variables.

## 👤 Author

- Hesham Eisa
- GitHub: [@HishamLB](https://github.com/HishamLB)
