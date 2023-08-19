from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder, format='PNG', dpi=300):
    images = convert_from_path(pdf_path, dpi=dpi)
    
    for idx, image in enumerate(images):
        image_path = f"{output_folder}/page_{idx + 1}.{format.lower()}"
        image.save(image_path, format=format)
        print(f"Page {idx + 1} saved as {image_path}")

pdf_path = "supreme_court.pdf"  # Replace with your PDF file path
output_folder = "output_images"  # Replace with desired output folder path
convert_pdf_to_images(pdf_path, output_folder)
