from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_review(story, styles):
    story.append(Paragraph("Book Review & Synthesis Template", styles["Heading1"]))
    story.append(Spacer(1, 10))
    template = "<b>Title & Author:</b> ___________________________<br/><b>Core Thesis:</b> ____________________________________<br/><b>Top 3 Key Takeaways:</b><br/>1. ____________________________________________<br/>2. ____________________________________________<br/>3. ____________________________________________<br/><br/><b>Action Items:</b> _________________________________"
    story.append(Paragraph(template, styles["Normal"]))
    story.append(PageBreak())

