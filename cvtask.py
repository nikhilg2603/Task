# import fitz  # PyMuPDF

# def pdf_to_text_with_formatting(pdf_path, output_txt_path):
#     doc = fitz.open(pdf_path)
#     text_with_formatting = ""

#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num)
#         text_with_formatting += page.get_text("text")

#     with open(output_txt_path, "w", encoding="utf-8") as txt_file:
#         txt_file.write(text_with_formatting)

#     doc.close()

# pdf_path = "supreme_court.pdf"  # Replace with your PDF file path
# output_txt_path = "output.txt"  # Replace with desired output text file path
# pdf_to_text_with_formatting(pdf_path, output_txt_path)
import pytesseract
from pdf2image import convert_from_path

def pdf_to_text_with_ocr(pdf_path, output_txt_path):
    images = convert_from_path(pdf_path)
    text_with_font_info = ""

    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')
        text_with_font_info += text + "\n"

    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text_with_font_info)

pdf_path = "supreme_court.pdf"  # Replace with your PDF file path
output_txt_path = "output_with_ocr.txt"  # Replace with desired output text file path
pdf_to_text_with_ocr(pdf_path, output_txt_path)
