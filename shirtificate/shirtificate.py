from fpdf import FPDF
pdf=FPDF()
pdf=FPDF(orientation='P',format='A4')
pdf.add_page()
pdf.set_font("times",size=40,style='B')
pdf.cell(200,20,txt="CS50 Shirtificate",ln=1,align='C')
pdf.image("shirtificate.png",y=60,x=20,w=180,h=170)
name=input("Name: ")
pdf.set_font("times",size=25)
pdf.set_text_color(255,255,255)
pdf.set_xy(50,130)
pdf.cell(100,20,txt=name+" took CS50",ln=1,align='C')
pdf.output("shirtificate.pdf")
