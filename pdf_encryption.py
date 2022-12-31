from PyPDF2 import PdfFileWriter, PdfFileReader


if __name__ == '__main__':
    pdf_writer = PdfFileWriter()
    pdf_doc = PdfFileReader('references.pdf')
    for page in range(pdf_doc.numPages):
        pdf_writer.add_page(pdf_doc.pages[page])

    password = input('Enter the password: ')
    pdf_writer.encrypt(password)
    with open('encrypted.pdf', 'wb') as file:
        pdf_writer.write(file)
    print('The file has been encrypted')
