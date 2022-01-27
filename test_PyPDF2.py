from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=A4)
can.setFont('Helvetica', 8)
can.drawString(0, 1, "NDT V1.0 © 2021")
can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("p.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
# for i in range(existing_pdf.getNumPages()):
n_page = existing_pdf.getNumPages()
for i in range(n_page-1):
    page = existing_pdf.getPage(i)
    page.mergePage(new_pdf.getPage(i))
    output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
