
from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_second_brain(story, styles):
    story.append(Paragraph("Building a Second Brain (CODE Framework)", styles["Heading1"]))
    story.append(Spacer(1, 10))
    content = "<b>C - Capture:</b> Keep what resonates.<br/><b>O - Organize:</b> Save for actionability.<br/><b>D - Distill:</b> Find the essence.<br/><b>E - Express:</b> Show your work and produce value."
    story.append(Paragraph(content, styles["Normal"]))
    story.append(PageBreak())

