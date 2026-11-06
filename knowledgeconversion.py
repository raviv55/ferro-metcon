from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_knowledge_conversion(story, styles):
    story.append(Paragraph("Knowledge Conversion Framework", styles["Heading1"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Book -> Information -> Understanding -> Knowledge -> Application -> Wisdom", styles["Title"]))
    story.append(Spacer(1, 15))
    desc = "Transforming static textual data into practical wisdom requires active filtering, continuous practical application, and contextual synthesis over time."
    story.append(Paragraph(desc, styles["Normal"]))
    story.append(PageBreak())


