import requests
import io
import os
import re
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)


def get_file_id(url):
    """Extracts the ID from a Google Drive link using a Regular Expression."""
    match = re.search(r"/d/([a-zA-Z0-9-_]+)", url)
    return match.group(1) if match else None


def run_app():
    print("="*52)
    print("☠️ WELCOME TO THE CLOUD-AI SCRAPER By:ALT ☠️")
    print("="*52)

    raw_url = input("\nPaste the Google Drive Link: ")
    file_id = get_file_id(raw_url)

    if not file_id:
        print("❌ Error: Invalid Google Drive URL.")
        return

    # Direct download link construction
    download_url = f'https://drive.google.com/uc?export=download&id={file_id}'

    print("\nConnecting to Google Drive...")
    response = requests.get(download_url)

    # Check if the file is accessible/public
    if response.status_code != 200:
        print("\n" + "!"*50)
        print("⚠️  ACCESS DENIED!")
        print("Please ensure the file is set to: 'Anyone with the link'")
        print("!"*50)
        return

    try:
        pdf_file = io.BytesIO(response.content)
        reader = PdfReader(pdf_file)
        document_text = "".join([page.extract_text() for page in reader.pages])

        print(f"✅ Success! Document read ({len(document_text)} characters).")
        print("You can now ask questions. Type 'exit' to quit.")

        while True:
            user_question = input("\nYour Question: ")
            if user_question.lower() in ['exit', 'quit']:
                break

            reply = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Context: {document_text}\n\nQuestion: {user_question}"
            )
            print(f"\nGEMINI: {reply.text}")

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")


if __name__ == "__main__":
    run_app()
