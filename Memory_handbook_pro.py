from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from automaticforgettingcurve import create_forgetting_curve
from finalbuild import build_book
styles=getSampleStyleSheet();story=[];create_forgetting_curve();build_book(story,styles);SimpleDocTemplate("AI_Guruji_Memory_Handbook_Complete.pdf",pagesize=A4).build(story);print("done")
