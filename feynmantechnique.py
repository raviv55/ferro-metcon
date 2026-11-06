from reportlab.platypus import Paragraph, PageBreak, Spacer

def get_chapter_data():
    title = 'Feynman Technique'
    content = "The Feynman Technique was developed by physicist Richard Feynman.<br/><br/><b>Step 1:</b> Learn a concept.<br/><b>Step 2:</b> Explain it in simple language.<br/><b>Step 3:</b> Identify gaps in understanding.<br/><b>Step 4:</b> Return to the source material.<br/><b>Step 5:</b> Simplify and teach again.<br/><br/><b>Practical Example:</b><br/>Suppose you are studying a submerged arc furnace in ferro-alloy production.<br/>Explain the furnace operation as if teaching a new graduate engineer.<br/>If the explanation becomes difficult, the knowledge gap has been discovered.<br/><br/><b>Advantages:</b><br/>&bull; Deep understanding<br/>&bull; Better retention<br/>&bull; Better teaching ability<br/>&bull; Better decision making"
    image_path = None
    return title, content, image_path

def add_feynman(story, styles):
    title, content, _ = get_chapter_data()
    story.append(Paragraph(title, styles["Heading1"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(content, styles["Normal"]))
    story.append(PageBreak())