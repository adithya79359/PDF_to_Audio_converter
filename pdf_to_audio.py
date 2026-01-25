import pdfplumber
from gtts import gTTS

pdf_path = input("Enter PDF file path: ")

text = ""

try:
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        print("No readable text found in PDF")
    else:
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        print("PDF converted to audio successfully")

except Exception as e:
    print("Error:", e)
