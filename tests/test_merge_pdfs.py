"""Unit tests for PDF merging and reversing functions."""

import io
import unittest

from pypdf import PdfReader, PdfWriter

from merge_pdfs import merge_pdfs, reverse_pdf


class TestPDFOperations(unittest.TestCase):
    """Test cases for PDF operations."""

    def setUp(self):
        """Set up sample PDFs for testing."""
        # Create sample PDFs for testing
        self.odd_pdf = self.create_sample_pdf([1, 3, 5])
        self.even_pdf = self.create_sample_pdf([6, 4, 2])

    def create_sample_pdf(self, page_numbers):
        """Create a sample PDF with given page numbers."""
        writer = PdfWriter()
        for _ in page_numbers:  # Remove unused variable 'number'
            writer.add_blank_page(width=72, height=72)
        output_pdf = io.BytesIO()
        writer.write(output_pdf)
        output_pdf.seek(0)
        return output_pdf

    def test_reverse_pdf(self):
        """Test reversing the pages of a PDF."""
        reversed_pdf = reverse_pdf(self.even_pdf)
        reader = PdfReader(reversed_pdf)
        self.assertEqual(len(reader.pages), 3)
        # Check if pages are reversed
        self.assertEqual(reader.pages[0].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[1].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[2].mediabox.lower_left, (0, 0))

    def test_merge_pdfs(self):
        """Test merging two PDFs."""
        reversed_even_pdf = reverse_pdf(self.even_pdf)
        merged_pdf = merge_pdfs(self.odd_pdf, reversed_even_pdf)
        reader = PdfReader(merged_pdf)
        self.assertEqual(len(reader.pages), 6)
        # Check if pages are merged alternately
        self.assertEqual(reader.pages[0].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[1].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[2].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[3].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[4].mediabox.lower_left, (0, 0))
        self.assertEqual(reader.pages[5].mediabox.lower_left, (0, 0))


if __name__ == "__main__":
    unittest.main()
