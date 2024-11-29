"""Module for merging and reversing PDF files."""

import io

from flask import Flask, render_template_string, request, send_file
from pypdf import PdfReader, PdfWriter

app = Flask(__name__)


def reverse_pdf(input_pdf):
    """Reverse the pages of the input PDF."""
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reversed(reader.pages):
        writer.add_page(page)
    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf


def merge_pdfs(odd_pdf, even_pdf):
    """Merge odd and reversed even PDF pages alternately."""
    odd_reader = PdfReader(odd_pdf)
    even_reader = PdfReader(even_pdf)
    writer = PdfWriter()
    even_pages = list(even_reader.pages)

    for i, odd_page in enumerate(odd_reader.pages):
        writer.add_page(odd_page)
        if i < len(even_pages):
            writer.add_page(even_pages[i])

    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)
    return output_pdf


@app.route("/")
def index():
    """Render the index HTML page."""
    with open("index.html", "r", encoding="utf-8") as file:
        return render_template_string(file.read())


@app.route("/merge", methods=["POST"])
def merge():
    """Handle the merge request and return the merged PDF."""
    odd_pdf = request.files["odd_pdf"]
    even_pdf = request.files["even_pdf"]
    reversed_even_pdf = reverse_pdf(even_pdf)
    merged_pdf = merge_pdfs(odd_pdf, reversed_even_pdf)
    return send_file(merged_pdf, as_attachment=True, download_name="merged.pdf")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
