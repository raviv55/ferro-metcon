from reportlab.platypus import Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_dynamic_table(story, styles):
    """
    Dynamically generates a table with customizable rows and columns.
    You can easily modify the data list below to add/remove rows or columns.
    """
    story.append(Paragraph("Customizable Dynamic Data Table", styles["Heading1"]))
    story.append(Spacer(1, 10))

    # ==========================================
    # 1. DEFINE YOUR TABLE DATA (Rows & Columns)
    # ==========================================
    # You can add or remove items in this list to scale rows, 
    # and add items to each inner list to scale columns.
    table_data_raw = [
        ["Metric / Chapter", "Day 1", "Day 7", "Day 30", "Day 90", "Status"],  # Header Row
        ["Active Recall", "100%", "85%", "75%", "70%", "Mastered"],
        ["Spaced Repetition", "100%", "90%", "85%", "80%", "Optimal"],
        ["Feynman Technique", "Level 1", "Level 2", "Level 3", "Level 4", "Reviewed"],
        ["Second Brain CODE", "Capture", "Organize", "Distill", "Express", "Active"]
    ]

    # ==========================================
    # 2. AUTOMATED FORMATTING (Paragraph Wrapping)
    # ==========================================
    # Wraps text in Paragraph flowables so long text auto-wraps inside table cells
    cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#2D3748')
    )
    
    header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        textColor=colors.whitesmoke,
        fontName='Helvetica-Bold'
    )

    formatted_data = []
    for row_idx, row in enumerate(table_data_raw):
        formatted_row = []
        for col in row:
            # Use header style for the first row, regular style for data rows
            current_style = header_style if row_idx == 0 else cell_style
            formatted_row.append(Paragraph(str(col), current_style))
        formatted_data.append(formatted_row)

    # ==========================================
    # 3. TABLE STYLING & STRUCTURE
    # ==========================================
    # Automatically calculates column widths based on available page width (~515 pt for A4 with margins)
    num_cols = len(table_data_raw[0])
    col_width = 515.0 / num_cols
    col_widths = [col_width] * num_cols

    t = Table(formatted_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1A365D')),  # Header background color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),  # Light grey border grid
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')]) # Alternating row colors
    ]))

    story.append(t)
    story.append(PageBreak())