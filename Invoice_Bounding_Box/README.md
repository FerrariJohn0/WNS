# Invoice Bounding Box Detection using OpenCV and OCR

A Python-based document analysis application that detects and highlights important invoice sections using OpenCV, OCR (Tesseract), and Streamlit.

The project allows users to upload invoice PDF or Word documents and automatically draws bounding boxes around detected text regions such as invoice number, date, vendor details, totals, and tables.

---

# Features

- Upload invoice PDF or DOCX files
- Convert PDF pages into images
- Extract invoice text using Tesseract OCR
- Detect text regions and draw bounding boxes
- Color-coded section highlighting
- Interactive Streamlit web interface
- OpenCV-based image processing

---

# Technologies Used

- Python
- OpenCV
- Streamlit
- Tesseract OCR
- pdf2image
- Pillow (PIL)
- NumPy

---

# Project Structure

```bash
Invoice_Bounding_Box/
│
├── sample.py
├── requirements.txt
├── README.md
├── sample-invoice-template-PDF-3.pdf
└── screenshots/
```
