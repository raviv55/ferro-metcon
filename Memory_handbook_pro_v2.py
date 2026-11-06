import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import matplotlib.pyplot as plt

PDF_NAME = 'AI_Guruji_Memory_Handbook_v2.pdf'

def generate_forgetting_curve_chart():
    chart_filename = 'forgetting_curve.png'
    x = [0, 1, 7, 30, 90]
    without_review = [100, 60, 40, 20, 10]
    with_review = [100, 90, 85, 80, 70]

    plt.figure(figsize=(6, 3))
    plt.plot(x, without_review, 'r-o', label='Without Review')
    plt.plot(x, with_review, 'g-o', label='With Review')
    plt.title('Forgetting Curve')
    plt.xlabel('Days')
    plt.ylabel('Retention %')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(chart_filename, dpi=300)
    plt.close()
    return chart_filename

# --- Chapter Definitions ---
def chapter_cover():
    return 'Cover', 'Mastering Memory, Knowledge and Wisdom', None

def chapter_contents():
    content = '''1. Memory<br/>
    2. Recall<br/>
    3. Reading<br/>
    4. Wisdom<br/>
    5. Active Recall<br/>
    6. Spaced Repetition<br/>
    7. Feynman Technique'''
    return 'Contents', content, None

def chapter_why_people_forget():
    return 'Why People Forget', 'Memory weakens over time without structured retrieval and regular review.', None

def chapter_forgetting_curve():
    img = generate_forgetting_curve_chart()
    return 'Forgetting Curve', 'See the retention drop off over time without periodic review:', img

def chapter_active_recall():
    return 'Active Recall', 'Close the book and recall key concepts directly from memory to strengthen neural connections.', None

def chapter_spaced_repetition():
    return 'Spaced Repetition', 'Review information at increasing time intervals to solidify long-term memory.', None

def chapter_feynman_technique():
    content = '''The Feynman Technique was developed by physicist Richard Feynman.<br/><br/>
    <b>Step 1:</b> Learn a concept.<br/>
    <b>Step 2:</b> Explain it in simple language.<br/>
    <b>Step 3:</b> Identify gaps in understanding.<br/>
    <b>Step 4:</b> Return to the source material.<br/>
    <b>Step 5:</b> Simplify and teach again.<br/><br/>
    <b>Practical Example:</b><br/>
    Suppose you are studying a submerged arc furnace in ferro-alloy production.<br/>
    Explain the furnace operation as if teaching a new graduate engineer.<br/>
    If the explanation becomes difficult, the knowledge gap has been discovered.<br/><br/>
    <b>Advantages:</b><br/>
    &bull; Deep understanding<br/>
    &bull; Better retention<br/>
    &bull; Better teaching ability<br/>
    &bull; Better decision making<br/><br/>
    The person who can explain a subject clearly usually understands it deeply.'''
    return 'Feynman Technique', content, None

# --- Main PDF Generator ---
def generate_pdf():
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1A365D'),
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        'ChapterBody',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=12
    )

    chapters = [
        chapter_cover,
        chapter_contents,
        chapter_why_people_forget,
        chapter_forgetting_curve,
        chapter_active_recall,
        chapter_spaced_repetition,
        chapter_feynman_technique,
    ]

    doc = SimpleDocTemplate(
        PDF_NAME,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    story = []

    for i, chapter_func in enumerate(chapters):
        title, content, img_path = chapter_func()
        
        story.append(Paragraph(title, title_style))
        story.append(Paragraph(content, body_style))
        
        if img_path:
            story.append(Image(img_path, width=400, height=200))
            story.append(Spacer(1, 10))
            
        # Add page break between chapters (except after the last chapter)
        if i < len(chapters) - 1:
            story.append(PageBreak())

    doc.build(story)
    print(f"Successfully generated new PDF: {os.path.abspath(PDF_NAME)}")

if __name__ == '__main__':
    # Delete old file to ensure clean overwrite
    if os.path.exists(PDF_NAME):
        try:
            os.remove(PDF_NAME)
        except PermissionError:
            print(f"\n[ERROR] Close '{PDF_NAME}' in your PDF reader first! Python cannot overwrite it while it is open.\n")
            exit()

    generate_pdf()