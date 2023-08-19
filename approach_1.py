import pytesseract
from pytesseract import Output
import cv2
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


def estimate_font_size(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    font_sizes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        font_size = w / 10.0  # This is a simple estimation based on contour width
        font_sizes.append(font_size)
def extract_text_and_font_size(image_path):
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image, config='--psm 6', output_type=Output.STRING)
    font_sizes = estimate_font_size(image)
    
    return text, font_sizes

def image_to_html(image_path, output_html_path):
    # Perform OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(Image.open(image_path))

    # Split extracted text into lines and maintain indentation
    lines = extracted_text.split('\n')
    indented_lines = [f'<div style="margin-left: {len(line.lstrip())}ch;">{line}</div>'
                      for line in lines]

    # Create an HTML file with indented lines
    with open(output_html_path, "w", encoding="utf-8") as html_file:
        html_file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Image to HTML</title>\n")
        html_file.write("<style>\n")
        html_file.write("div { font-family: Arial, sans-serif; }\n")  # Use a common font
        html_file.write("</style>\n</head>\n<body>\n")
        html_file.write('\n'.join(indented_lines))
        html_file.write("</body>\n</html>")

image_path = "image.jpg"  # Replace with your image file path
output_html_path = "output.html"  # Replace with desired output HTML file path
image_to_html(image_path, output_html_path)
