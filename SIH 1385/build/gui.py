from tkinter import Tk, Canvas, Entry, Text, Button, filedialog, PhotoImage, messagebox,OptionMenu, StringVar
from pathlib import Path
import PyPDF2
from googletrans import Translator
import pytesseract
from PIL import Image
from docx import Document
from fpdf import FPDF

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\Project 3\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

selected_file_paths = []
selected_language = ""
def select_language(value):
    global selected_language
    language_mapping = {
        "Hindi": "hi",
        "Bengali": "bn",
        "Telugu": "te",
        "Marathi": "mr",
        "Tamil": "ta",
        "Urdu": "ur",
        "Gujarati": "gu",
        "Kannada": "kn",
        "Odia (Oriya)": "or",
        "Punjabi": "pa",
        "Malayalam": "ml",
        "Assamese": "as"
    }
    selected_language = language_mapping.get(value, value)
def open_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        if selected_file_paths:
            messagebox.showinfo("Warning", "A file is already chosen.")
        selected_file_paths.append(file_path)

def open_word_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        if selected_file_paths:
            messagebox.showinfo("Warning", "A file is already chosen.")
        selected_file_paths.append(file_path)

def open_image_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg")])
    if file_path:
        if selected_file_paths:
            messagebox.showinfo("Warning", "A file is already chosen.")
        selected_file_paths.append(file_path)

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest=selected_language)
    translated_text = translation.text
    return translated_text

def translate_and_update_entry():
    text_to_translate = entry_2.get()
    translated_text = ""

    if text_to_translate:
        translated_text += translate_text(text_to_translate)
        entry_1.delete("1.0", "end")
        entry_1.insert("1.0", translated_text)

    if selected_file_paths:
        translated_text += "\n\n"  # Add a separator if both text and files are present

        for file_path in selected_file_paths:
            if file_path.lower().endswith('.pdf'):
                with open(file_path, "rb") as pdf_file:
                    pdf_reader = PyPDF2.PdfReader(pdf_file)
                    extracted_text = ""
                    for page_num in range(len(pdf_reader.pages)):
                        page = pdf_reader.pages[page_num]
                        page_text = page.extract_text()
                        extracted_text += page_text
            elif file_path.lower().endswith(('.doc', '.docx')):
                doc = Document(file_path)
                extracted_text = ""
                for paragraph in doc.paragraphs:
                    extracted_text += paragraph.text + "\n"
            elif file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                pytesseract.pytesseract.tesseract_cmd = 'C:/Users/RUPAM DAS/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
                image = Image.open(file_path)
                extracted_text = pytesseract.image_to_string(image)
            else:
                extracted_text = "Unsupported file type"
            
            translated_text += translate_text(extracted_text) + "\n"

    entry_1.delete("1.0", "end")
    entry_1.insert("1.0", translated_text)
    selected_file_paths.clear()

def save_translated_text():
    if entry_1.get("1.0", "end-1c"):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(entry_1.get("1.0", "end-1c"))

window = Tk()
window.geometry("814x592")
window.configure(bg="#3172D3")

canvas = Canvas(
    window,
    bg="#3172D3",
    height=592,
    width=814,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    407.0,
    296.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    402.5,
    394.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=71.0,
    y=301.0,
    width=663.0,
    height=184.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    404.0,
    210.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=126.0,
    y=194.0,
    width=556.0,
    height=30.0
)

canvas.create_text(
    127.0,
    165.0,
    anchor="nw",
    text="Type Something...",
    fill="#FFFFFF",
    font=("InriaSans Regular", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=window.quit,
    relief="flat"
)
button_1.place(
    x=600.0,
    y=247.0,
    width=157.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_pdf_file,
    relief="flat"
)
button_2.place(
    x=69.0,
    y=93.0,
    width=192.0,
    height=31.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_word_file,
    relief="flat"
)
button_3.place(
    x=305.0,
    y=94.0,
    width=191.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=translate_and_update_entry,
    relief="flat"
)
button_4.place(
    x=69.0,
    y=247.0,
    width=157.0,
    height=32.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=save_translated_text,
    relief="flat"
)
button_5.place(
    x=311.0,
    y=510.0,
    width=185.0,
    height=38.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_image_file,
    relief="flat"
)

button_6.place(
    x=566.0,
    y=93.0,
    width=191.0,
    height=31.0
)

canvas.create_text(
    134.0,
    59.0,
    anchor="nw",
    text="                      *~Translating to your language is now easy*~",
    fill="#FFFFFF",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    231.0,
    9.0,
    anchor="nw",
    text="The Mandarin Translator",
    fill="#FFFFFF",
    font=("KeaniaOne Regular", 32 * -1)
)

# Create a dropdown with the specified options
options = [
    "Hindi", "Bengali", "Telugu", "Marathi", "Tamil",
    "Urdu", "Gujarati", "Kannada", "Odia (Oriya)", "Punjabi", "Malayalam", "Assamese"
]

var = StringVar()
var.set(options[0])  # Default value
dropdown = OptionMenu(window, var, *options, command=select_language)
dropdown.config(width=20, height=1, font=("Arial", 12), padx=8, pady=8, relief="ridge")
dropdown.place(x=266, y=248)



window.resizable(False, False)
window.mainloop()
