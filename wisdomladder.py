from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_wisdom(story, styles):
    story.append(Paragraph("The DIKW Pyramid (Wisdom Ladder)", styles["Heading1"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Data -> Information -> Knowledge -> Understanding -> Wisdom", styles["Title"]))
    story.append(Spacer(1, 15))
    desc = "<b>Data:</b> Raw facts & symbols.<br/><b>Information:</b> Contextualized data.<br/><b>Knowledge:</b> Actionable understanding.<br/><b>Wisdom:</b> Evaluated judgment and deep principle mastery."
    story.append(Paragraph(desc, styles["Normal"]))
    story.append(PageBreak())

