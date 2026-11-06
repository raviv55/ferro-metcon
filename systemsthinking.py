
from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_systems(story, styles):
    story.append(Paragraph("Systems Thinking & Feedback Loops", styles["Heading1"]))
    story.append(Spacer(1, 10))
    content = "Understanding interconnected mental models, reinforcing feedback loops, balancing loops, and root cause analysis."
    story.append(Paragraph(content, styles["Normal"]))
    story.append(PageBreak())

