from fpdf import FPDF
mypdf=FPDF()
mypdf.add_page()
mypdf.set_font('Arial','B',18)
x="hello"
mypdf.cell(40,10,x)
mypdf.output('mypdfdemo.pdf','F')

