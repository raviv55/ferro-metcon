from reportlab.platypus import Paragraph, Spacer, PageBreak

def add_cover(story, styles):
    story.append(Paragraph("MASTERING MEMORY, KNOWLEDGE & WISDOM", styles["Title"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("AI Guruji Signature Edition", styles["Heading2"]))
    story.append(Spacer(1, 20))
    story.append(PageBreak())


