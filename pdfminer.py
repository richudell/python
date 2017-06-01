from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter,TextConverter,XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

def convert(case,fname, pages=None):
    if not pages: pagenums = set();
    else:         pagenums = set(pages);      
    manager = PDFResourceManager() 
    codec = 'utf-8'
    caching = True

    if case == 'text' :
        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams())     
    if case == 'HTML' :
        output = io.BytesIO()
        converter = HTMLConverter(manager, output, codec=codec, laparams=LAParams())

    interpreter = PDFPageInterpreter(manager, converter)   
    infile = open(fname, 'rb')

    for page in PDFPage.get_pages(infile, pagenums,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    convertedPDF = output.getvalue()  

    infile.close(); converter.close(); output.close()
    return convertedPDF

#//////////// main ///////////////////////
filePDF  = '170525.pdf'     # input
fileHTML = '170525.pdf.html'   # output
fileTXT  = '170525.pdf.txt'     # output

case = "text"

if case == 'HTML' :
    convertedPDF = convert('HTML', filePDF, pages=[0,1])
    fileConverted = open(fileHTML, "wb")
if case == 'text' :
    convertedPDF = convert('text', filePDF, pages=[0,1])
    fileConverted = open(fileTXT, "w")

fileConverted.write(convertedPDF)
fileConverted.close()
#print(convertedPDF) 