# 🧠 RAG Model with CLIP for Multimodal Retrieval & PDF Generation

This project combines a Retrieval-Augmented Generation (RAG) approach with OpenAI's CLIP model to extract, embed, and reason over both **text** and **images** from web content (HTML or PDF). It answers questions based on the content and generates a visually enriched **PDF report** with embedded images.

---

## 🚀 Features

- 🔎 **Web Content Extraction**: Extracts both text and images from URLs (HTML pages or PDF documents)
- 🧠 **Multimodal Embeddings**: Uses CLIP to create embeddings for both text and image content
- 🔍 **Similarity-Based Retrieval**: Finds most relevant content chunks based on semantic similarity
- 🤖 **Question Answering**: Provides answers based on retrieved context from multimodal content
- 📄 **Rich PDF Generation**: Creates comprehensive reports with:
  - ✅ Detailed answers
  - 📌 Top retrieved text and image chunks
  - 🖼️ Embedded image previews (not just links)
  - 📊 Relevance scores and metadata

---

## 📋 Requirements

- Python 3.8+
- CUDA-compatible GPU (optional, but recommended for faster processing)
- Internet connection (for downloading CLIP model weights on first run)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd rag-clip-multimodal
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Verify Installation
```bash
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import clip; print('CLIP installed successfully')"
```

---

## 📄 Usage

### 🧪 Run the Application
```bash
python app.py
```

### ✍️ Input Requirements
When prompted, provide:
1. **URL**: Web page (HTML) or PDF document URL
   - Example: `https://example.com/article.html`
   - Example: `https://example.com/document.pdf`
2. **Question**: Your question about the content
   - Example: "What are the main findings discussed in this document?"
   - Example: "Describe the images and their relevance to the topic"

### 📤 Expected Output
The system will:
1. **Extract Content**: Download and process text + images from the URL
2. **Generate Embeddings**: Create CLIP embeddings for multimodal content
3. **Retrieve Context**: Find most relevant chunks based on your question
4. **Generate Answer**: Provide a comprehensive response
5. **Create PDF Report**: Generate `output.pdf` containing:
   - Your original question
   - Detailed answer with context
   - Top retrieved text chunks with relevance scores
   - Embedded images with captions
   - Processing metadata and statistics

---

## 📚 Project Structure

```
rag-clip-multimodal/
├── 📄 README.md              # This file
├── 📄 requirements.txt       # Python dependencies
├── 🐍 app.py                # Main application runner
├── 🔧 clip_utils.py         # CLIP model loading and embedding utilities
├── 📝 text_utils.py         # Text extraction, chunking, and processing
├── 🖼️ image_utils.py        # Image extraction and embedding functions
├── 📑 pdf_utils.py          # PDF generation with multimodal content
├── 📊 output.pdf            # Generated report (created after running)
└── 🗂️ temp/                 # Temporary files (auto-created)
```

---

## 🧠 How It Works

### 1. **Content Extraction**
- **HTML Pages**: Uses BeautifulSoup to extract text content and image URLs
- **PDF Documents**: Extracts text using PyPDF2 and processes embedded images
- **Text Processing**: Cleans, chunks, and preprocesses text for optimal embedding

### 2. **Multimodal Embedding**
- **CLIP Integration**: Leverages OpenAI's CLIP model for unified text-image embeddings
- **Text Embeddings**: Converts text chunks into high-dimensional vectors
- **Image Embeddings**: Downloads images and creates visual embeddings
- **Similarity Matching**: Uses cosine similarity for retrieval ranking

### 3. **Question Answering**
- **Context Retrieval**: Finds top-K most relevant text and image chunks
- **Answer Generation**: Combines retrieved context to formulate comprehensive answers
- **Multimodal Reasoning**: Considers both textual and visual information

### 4. **PDF Report Generation**
- **Rich Formatting**: Professional layout with headers, sections, and styling
- **Image Integration**: Embeds actual images (not just descriptions)
- **Metadata Inclusion**: Relevance scores, chunk sources, and processing statistics
- **Structured Output**: Organized sections for easy navigation

---

## 🛠️ Configuration Options

### Environment Variables (Optional)
```bash
# Set custom model cache directory
export CLIP_CACHE_DIR="/path/to/cache"

# Configure processing parameters
export MAX_TEXT_CHUNKS=50
export MAX_IMAGES=20
export TOP_K_RESULTS=10
```

### Model Configuration
Edit `clip_utils.py` to customize:
- CLIP model variant (`ViT-B/32`, `ViT-B/16`, `ViT-L/14`)
- Device selection (auto-detects GPU/CPU)
- Batch processing sizes

---

## 🐛 Troubleshooting

### ❌ Common Issues & Solutions

**PermissionError: output.pdf**
```bash
# Solution: Close any PDF viewers and ensure write permissions
chmod 755 .
lsof output.pdf  # Check if file is in use
```

**CLIP model download fails**
```bash
# Solution: Check internet connection and clear cache
rm -rf ~/.cache/clip
python -c "import clip; clip.load('ViT-B/32')"
```

**Out of memory errors**
```bash
# Solution: Reduce batch sizes or use CPU
export CUDA_VISIBLE_DEVICES=""  # Force CPU usage
```

**SSL certificate errors**
```bash
# Solution: Update certificates or bypass for testing
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
```

**Image download failures**
- Check if images require authentication
- Verify image URLs are accessible
- Some sites block automated image downloads

---

## ⚡ Performance Tips

### 🚀 Speed Optimization
- **GPU Usage**: Ensure CUDA is available for faster embedding generation
- **Batch Processing**: Process multiple items simultaneously
- **Caching**: CLIP models are cached after first download
- **Image Preprocessing**: Resize large images to reduce processing time

### 💾 Memory Management
- **Chunk Size**: Adjust text chunk sizes based on available RAM
- **Image Limits**: Set maximum number of images to process
- **Model Selection**: Use smaller CLIP variants for lower memory usage

---

## 🔧 Advanced Configuration

### Custom Text Processing
```python
# In text_utils.py, modify chunking parameters:
CHUNK_SIZE = 500          # Characters per chunk
CHUNK_OVERLAP = 50        # Overlap between chunks
MIN_CHUNK_LENGTH = 100    # Minimum chunk size
```

### Image Processing Settings
```python
# In image_utils.py, adjust image parameters:
MAX_IMAGE_SIZE = (512, 512)  # Resize large images
SUPPORTED_FORMATS = ['.jpg', '.png', '.gif', '.webp']
MAX_IMAGES_PER_PAGE = 20     # Limit images processed
```

---

## 📊 Output Examples

### Sample PDF Report Structure
```
📄 RAG Analysis Report
├── 🔍 Question: "What are the key findings?"
├── 💡 Answer: [Comprehensive response based on retrieved content]
├── 📝 Top Text Chunks:
│   ├── Chunk 1 (Score: 0.89): [Text content...]
│   ├── Chunk 2 (Score: 0.85): [Text content...]
│   └── ...
├── 🖼️ Relevant Images:
│   ├── Image 1 (Score: 0.76): [Embedded image with caption]
│   ├── Image 2 (Score: 0.71): [Embedded image with caption]
│   └── ...
└── 📊 Processing Statistics:
    ├── Total text chunks: 45
    ├── Total images processed: 12
    ├── Processing time: 23.4s
    └── Model used: ViT-B/32
```

---

## 🔬 Technical Details

### CLIP Model Information
- **Architecture**: Vision Transformer + Text Transformer
- **Training**: Contrastive learning on 400M image-text pairs
- **Embedding Dimension**: 512 (ViT-B/32) or 768 (ViT-L/14)
- **Supported Languages**: Primarily English, limited multilingual support

### Similarity Computation
```python
# Cosine similarity between question and content embeddings
similarity = np.dot(question_embedding, content_embedding) / (
    np.linalg.norm(question_embedding) * np.linalg.norm(content_embedding)
)
```

---

## 🤝 Contributing

1. **Fork the Repository**
2. **Create Feature Branch**: `git checkout -b feature/amazing-feature`
3. **Commit Changes**: `git commit -m 'Add amazing feature'`
4. **Push to Branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include unit tests for new features
- Update README for significant changes

---

## 📈 Roadmap

### Upcoming Features
- [ ] **Multi-language Support**: Extend beyond English content
- [ ] **Video Processing**: Extract frames and audio from video URLs
- [ ] **Database Integration**: Store embeddings for faster retrieval
- [ ] **Web Interface**: Flask/Streamlit GUI for easier interaction
- [ ] **Batch Processing**: Handle multiple URLs simultaneously
- [ ] **API Endpoints**: RESTful API for programmatic access

### Performance Improvements
- [ ] **Async Processing**: Parallel content extraction and embedding
- [ ] **Model Optimization**: Quantized models for faster inference
- [ ] **Smart Caching**: Avoid reprocessing identical content
- [ ] **Progressive Loading**: Stream results as they're processed

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **OpenAI**: For the incredible CLIP model
- **PyTorch Team**: For the deep learning framework
- **Hugging Face**: For model hosting and transformers library
- **Community Contributors**: For feedback and improvements

---


## 🏷️ Keywords

`RAG` `CLIP` `Multimodal` `Retrieval` `AI` `Machine Learning` `Computer Vision` `NLP` `PDF Generation` `Web Scraping` `Embeddings` `Similarity Search` `Question Answering`

---

**Made with ❤️ and lots of ☕ by [Syed Peer]**

*Happy retrieving! 🚀*
