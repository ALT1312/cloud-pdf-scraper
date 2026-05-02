# GOOGLE DRIVE AI CHATBOT (2026)

This project connects a Google Drive PDF to the Gemini AI API for real-time questioning.

Setup:
1. Ensure .env has; GOOGLE_API_KEY.
2. Ensure file_id is set to a public Google Drive PDF.
3. Run: python3 cloud_scraper.py

-----------------------------
This script downloads a public PDF from Google Drive, 
extracts the text, and starts an interactive chat session using ** Gemini 2.5 Flash **.

## 🚀 Quick Start
1. **Install Dependencies**:
   ```bash
   pip install requests pypdf google-genai python-dotenv

2. Create a .env file and add your Google API key:
GOOGLE_API_KEY=your_key_here

3. Run the App:
python3 cloud_scraper.py

## 🛠 Usage
1. Run the script: `python3 cloud_scraper.py`
2. When prompted, paste a **PUBLIC** Google Drive PDF link.
3. Chat with the AI about the document!