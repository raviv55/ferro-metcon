
from reportlab.platypus import Paragraph, Image, PageBreak, Spacer

def add_curve(story, styles):
    story.append(Paragraph("Forgetting Curve", styles["Heading1"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Memory weakens over time without structured retrieval and regular review. Below is the visualization of retention over 90 days:", styles["Normal"]))
    story.append(Spacer(1, 10))
    story.append(Image("forgetting_curve.png", width=400, height=200))
    story.append(PageBreak())

