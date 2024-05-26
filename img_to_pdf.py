import os
import fitz

def merge(directory_path, output_pdf_path):
    pdf_document = fitz.open()

    valid_image_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif']
    image_files = [f for f in os.listdir(directory_path) if os.path.splitext(f)[1].lower() in valid_image_extensions]
    
    # currently sorting by name
    image_files.sort()

    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        image = fitz.open(image_path)
        rect = image[0].rect
        pdf_page = pdf_document.new_page(width=rect.width, height=rect.height)
        pdf_page.insert_image(rect, filename=image_path)
    
    pdf_document.save(output_pdf_path)
    pdf_document.close()
