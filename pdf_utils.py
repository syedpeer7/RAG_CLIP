from fpdf import FPDF
import os
import requests
from io import BytesIO
from PIL import Image
import re


def save_output_to_pdf(url, query, answer, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # ✅ Use a Unicode font
    font_path = "DejaVuSans.ttf"
    if not os.path.exists(font_path):
        raise FileNotFoundError("Please place 'DejaVuSans.ttf' in your project folder.")

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    # 📝 Write basic info
    pdf.multi_cell(0, 10, f"Source URL: {url}")
    pdf.ln()
    pdf.multi_cell(0, 10, f"Query: {query}")
    pdf.ln()

    # 🔍 Extract image URLs (jpg/png/jpeg/webp/gif)
    image_urls = re.findall(r'(https?://\S+\.(?:jpg|jpeg|png|webp|gif))', answer)

    # 🧠 Remove image links from answer text
    clean_answer = answer
    for img_url in image_urls:
        clean_answer = clean_answer.replace(img_url, '')

    # 🖊️ Write the answer (without links)
    pdf.multi_cell(0, 10, "Answer:")
    pdf.multi_cell(0, 10, clean_answer.strip())
    pdf.ln()

    # 🖼️ Add images to PDF
    for img_url in image_urls:
        try:
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))

            # Save image temporarily
            temp_img_path = "temp_img.jpg"
            img.convert("RGB").save(temp_img_path)

            # Scale image width to page
            pdf.image(temp_img_path, w=170)
            pdf.ln(10)

            os.remove(temp_img_path)
        except Exception as e:
            pdf.multi_cell(0, 10, f"[Image failed to load: {img_url}]")

    pdf.output(filename)
    return filename
