# 🏥 AI Healthcare Chatbot

An AI-powered healthcare chatbot that answers health-related questions using a local disease database and OpenRouter's GPT API as a fallback. Built with Python and Flask.

> ⚠️ For educational purposes only. Does not provide medical diagnosis. Always consult a healthcare professional.

## ✨ Features

- Disease and symptom info from a local JSON database
- AI-powered responses for queries not in the database
- PDF report generation
- Simple CLI and web interface via Flask

## 🛠️ Tech Stack

Python, Flask, OpenRouter API (GPT), JSON, dotenv

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/jayantgulia2005-cmyk/AI-HEALTHCARE-CHATBOT.git
cd AI-HEALTHCARE-CHATBOT

# Install dependencies
pip install -r requirements.txt

# Add your API key — create a .env file
open_router_api=your_openrouter_api_key_here

# Run CLI
python main.py

# Or run web app
python app.py
```

## 📁 Project Structure
