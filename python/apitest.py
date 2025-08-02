from reportlab.pdfgen import canvas
import os
file_name = str(input('input file name-> '))
if '.pdf' in file_name:
    file_path = os.getcwd() + '/' + file_name
    c = canvas.Canvas(file_path)
    c.drawString(100,750,'Code made pdf file')
    c.save()
    print(file_name , ' file created successfully')






else:
    print('error', 'enter extension .pdf')


