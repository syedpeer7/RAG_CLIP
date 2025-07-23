from scraper import scrape_webpage
from image_utils import download_images
from embedder import get_avg_clip_embedding_from_long_text, load_clip_model
from generator import generate_with_gemini
from pdf_utils import save_output_to_pdf
import os

def run_rag(url, query):
    text, img_urls = scrape_webpage(url)
    images = download_images(img_urls)

    model_clip, preprocess, device = load_clip_model()

    # ✅ Use averaged chunk embeddings for long text
    text_embedding = get_avg_clip_embedding_from_long_text(
        text=text, model=model_clip, device=device
    )

    answer = generate_with_gemini(text, img_urls, query)

    # ✅ Save the answer to a PDF
    pdf_path = save_output_to_pdf(url, query, answer)

    return f"Answer saved to PDF: {pdf_path}"

if __name__ == "__main__":
    url = input("Enter website URL: ")
    query = input("Enter your question: ")
    print(run_rag(url, query))
