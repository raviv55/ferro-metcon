from reportlab.platypus import Paragraph, PageBreak, Spacer

def add_memory_palace(story, styles):
    story.append(Paragraph("Method of Loci (Memory Palace)", styles["Heading1"]))
    story.append(Spacer(1, 10))
    content = "The Memory Palace technique leverages spatial visual memory by anchoring concepts to familiar physical locations.<br/><br/><b>Steps:</b><br/>1. Select a familiar place.<br/>2. Define a clear walking path.<br/>3. Associate vivid mental images with spatial anchors."
    story.append(Paragraph(content, styles["Normal"]))
    story.append(PageBreak())

