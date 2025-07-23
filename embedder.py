import clip
import torch
import numpy as np

def load_clip_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    return model, preprocess, device

def get_clip_embedding(text=None, image=None, model=None, preprocess=None, device=None):
    if text:
        tokens = clip.tokenize([text[:500]]).to(device)  # truncate long text to avoid token limit
        with torch.no_grad():
            return model.encode_text(tokens).cpu().numpy()[0]
    elif image:
        img_tensor = preprocess(image).unsqueeze(0).to(device)
        with torch.no_grad():
            return model.encode_image(img_tensor).cpu().numpy()[0]

# ✅ NEW: Average embeddings for long text
def get_avg_clip_embedding_from_long_text(text, model, device, max_tokens=77):
    # Split the text into small chunks based on sentence or newlines
    chunks = text.split('. ')
    embeddings = []

    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            tokens = clip.tokenize([chunk[:500]]).to(device)
            with torch.no_grad():
                emb = model.encode_text(tokens).cpu().numpy()[0]
                embeddings.append(emb)
        except:
            continue

    if embeddings:
        return np.mean(embeddings, axis=0)
    else:
        return None
