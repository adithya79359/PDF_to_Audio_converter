from pdf2image import convert_from_path
import pytesseract
from gtts import gTTS

# ✅ Tell pytesseract where tesseract.exe is
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Tell pdf2image where Poppler is
POPPLER_PATH = r"C:\poppler-24.02.0\Library\bin"

pdf_path = input("Enter PDF path: ")

images = convert_from_path(
    pdf_path,
    poppler_path=POPPLER_PATH
)

full_text = ""

for img in images:
    full_text += pytesseract.image_to_string(img) + "\n"

if not full_text.strip():
    print("No text found in PDF")
else:
    gTTS(text=full_text, lang="en").save("output.mp3")
    print("PDF converted to audio successfully")
