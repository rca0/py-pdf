from reportlab.pdfgen import canvas


def _generatePDF(data_list): 
    try:
        pdf_name = input("Set the pdf name file: ")
        pdf = canvas.Canvas('{}.pdf'.format(pdf_name))
        x = 720
        for name, age in data_list.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(name, age))
            
        pdf.setTitle(pdf_name)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, "Customers")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, "Name and Age")
        pdf.save()
    except Exception as err:
        print("Error when generate PDF file: {}.pdf".format(pdf_name))
        raise err


if __name__ == '__main__':
    # here, there are infinitely possible to get informations from everywhere like:
    # databases, APIs, excel/doc files and so on...
    _generatePDF({
        'José': 33,
        'João': 34,
        'Maria': 21,
        'Flash': 26,
        'Batman': 21,
        'Mariana': 23,
        'Elon': 40,
    })