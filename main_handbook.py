import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Import the forgetting curve generator and master builder function
from automaticforgettingcurve import create_forgetting_curve
from finalbuild import build_book

PDF_NAME = 'AI_Guruji_Memory_Handbook_v2.pdf'

def main():
    # 1. Close/Remove old PDF file if it exists to avoid Windows file-lock errors
    if os.path.exists(PDF_NAME):
        try:
            os.remove(PDF_NAME)
        except PermissionError:
            print(f"\n[ERROR] Close '{PDF_NAME}' in your PDF reader first!\n")
            return

    # 2. Automatically generate the chart image before building PDF
    create_forgetting_curve()

    # 3. Setup document and styles
    doc = SimpleDocTemplate(
        PDF_NAME,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    story = []

    # 4. Append all chapters sequentially using your existing build_book structure
    build_book(story, styles)

    # 5. Render final PDF
    doc.build(story)
    print(f"Successfully generated complete handbook: {os.path.abspath(PDF_NAME)}")

if __name__ == '__main__':
    main()