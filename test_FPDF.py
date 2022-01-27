from fpdf import FPDF


class Pdf(FPDF):
    def header(self):
        # 'image', x, y, width of image
        self.image('pgcb1.png', 10, 3, 25)
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'Title', border=False, ln=True, align='C')
        self.ln(10)


#  p-portrait , scale-mm, size-A$
pdf = Pdf('l', 'mm', 'A4')
# pdf = Pdf.open('p.pdf')
pdf.add_page()
# font = helvetica, style = '' for default regular, font size=12
pdf.set_font('helvetica', '', 12)
pdf.cell(40, 10, 'lol', ln=True)
pdf.cell(80, 10, 'lols', ln=True)
pdf.set_text_color(0, 256, 0)
pdf.cell(80, 12, 'lols', ln=True)
for i in range(40):
    pdf.cell(0, 10, f'line {i}', ln=True)
pdf.output('pdf_1.pdf')
