
from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_reading_levels(story, styles):
    story.append(Paragraph("Four Levels of Reading", styles["Heading1"]))
    story.append(Spacer(1, 10))
    content = "<b>1. Elementary Reading:</b> Basic literacy.<br/><br/><b>2. Inspectional Reading:</b> Systematic skimming.<br/><br/><b>3. Analytical Reading:</b> Deep reading & structural critique.<br/><br/><b>4. Syntopical Reading:</b> Comparative synthesis."
    story.append(Paragraph(content, styles["Normal"]))
    story.append(PageBreak())


