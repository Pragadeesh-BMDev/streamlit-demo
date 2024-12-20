import streamlit as st
import base64

import fitz  # PyMuPDF
import os
import time

class coordinates:
    page_number : int
    points: tuple[int, int, int, int]

    def __init__(self, points, page_number):
        self.points = points
        self.page_number = page_number

def highlight_area_on_pdf(pdf_path, output_path, coordinates : list[coordinates], highlight_color=(1, 1, 0)):
    """
    Highlights specific areas on a PDF page (e.g., over an image).

    :param pdf_path: Path to the input PDF file
    :param output_path: Path to save the modified PDF
    :param page_number: The page number (0-indexed) where the highlight will be applied
    :param coordinates: A list of tuples [(x0, y0, x1, y1)] defining rectangle coordinates
    :param highlight_color: Tuple with RGB values for the highlight color (0 to 1 scale)
    """
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Ensure coordinates are provided
    if not coordinates:
        print("No coordinates provided for highlighting. Exiting.")
        pdf_document.close()
        return

    # Iterate over all rectangles to highlight
    for coordinate in coordinates:
        try:
            # Check if the page exists
            if coordinate.page_number < 0 or coordinate.page_number >= len(pdf_document):
                pdf_document.close()
                raise ValueError(f"Invalid page number: {coordinate.page_number}. The PDF has {len(pdf_document)} pages.")

            # Get the specified page
            page = pdf_document[coordinate.page_number]

            highlight_rect = fitz.Rect(coordinate.points)
            # Add a rectangle annotation with the highlight color
            highlight = page.add_rect_annot(highlight_rect)
            highlight.set_colors(stroke=highlight_color, fill=highlight_color)  # Fill and stroke color
            highlight.set_opacity(0.4)  # Make the highlight semi-transparent
            highlight.update()  # Apply changes
        except Exception as e:
            print(f"Error processing rectangle {coordinate.points}: {e}")

    # Save the modified PDF
    pdf_document.save(output_path, garbage=4, deflate=True)
    pdf_document.close()
    print(f"Highlight added and saved to: {output_path}")

# Example Usage
pdf_file = "77911_UK_10627575_12-2022.pdf"  # Input PDF file
output_file = "output.pdf"  # Output PDF file

coordinates_list : list[coordinates] = []
coordinates_list.append(coordinates((100, 100, 200, 200), 0))
coordinates_list.append(coordinates((100, 100, 200, 200), 20))

if not os.path.exists(pdf_file):
    print(f"File not found: {pdf_file}")
else:
    print("File found! Proceeding with highlight.")
    start_time = time.time()  
    highlight_area_on_pdf(pdf_file, output_file, coordinates_list)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total Time: {total_time:.2f} seconds")


# ------- streamlit code ------- 
st.set_page_config(layout="wide")


# Logo and Navigation
col1, col2 = st.columns([1, 1])
# with col2:
#     st.markdown(("# 30 Days of Streamlit"))


# Sidebar
st.sidebar.header(("About"))

# Display content

# Path to the PDF file
pdf_path = "highlighted_example1.pdf"

# Read the PDF file as binary
with open(pdf_path,"rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)
