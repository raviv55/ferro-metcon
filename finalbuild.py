
from coverpage import add_cover
from insertcurve import add_curve
from fourlevelsofreading import add_reading_levels
from knowledgeconversion import add_knowledge_conversion
from memorypalacepage import add_memory_palace
from feynmantechnique import add_feynman
from secondbrain import add_second_brain
from systemsthinking import add_systems
from bookreviewtemplate import add_review
from wisdomladder import add_wisdom

def build_book(story, styles):
    add_cover(story, styles)
    add_curve(story, styles)
    add_reading_levels(story, styles)
    add_knowledge_conversion(story, styles)
    add_memory_palace(story, styles)
    add_feynman(story, styles)
    add_second_brain(story, styles)
    add_systems(story, styles)
    add_review(story, styles)
    add_wisdom(story, styles)











