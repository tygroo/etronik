from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

def getPageByPage(pdf):
	# Open a PDF file.
	fp = open(pdf, 'rb')
	# Create a PDF parser object associated with the file object.
	parser = PDFParser(fp)
	
	# Create a PDF document object that stores the document structure.
	# Supply the password for initialization.
	document = PDFDocument(parser, password)
	
	# Check if the document allows text extraction. If not, abort.
	if not document.is_extractable:
		raise PDFTextExtractionNotAllowed
	
	# Create a PDF resource manager object that stores shared resources.
	rsrcmgr = PDFResourceManager()
	# Create a PDF device object.
	device = PDFDevice(rsrcmgr)
	# Create a PDF interpreter object.
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	# Process each page contained in the document.
	for page in PDFPage.create_pages(document):
		interpreter.process_page(page)

def getPageInPdf(pdf):
	# Open a PDF file.
	fp = open(pdf, 'rb')
	# Create a PDF parser object associated with the file object.
	parser = PDFParser(fp)
	
	# Create a PDF document object that stores the document structure.
	# Supply the password for initialization.
	document = PDFDocument(parser)
	
	# Check if the document allows text extraction. If not, abort.
	if not document.is_extractable:
		raise PDFTextExtractionNotAllowed
	
	# Create a PDF resource manager object that stores shared resources.
	rsrcmgr = PDFResourceManager()
	# Create a PDF device object.
	device = PDFDevice(rsrcmgr)
	# Create a PDF interpreter object.
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	# Process page.
	interpreter.process_page(page)

def obtainTable(pdf):
	# Open a PDF document.
	fp = open(pdf, 'rb')
	parser = PDFParser(fp)
	document = PDFDocument(parser)

	# Get the outlines of the document.
	outlines = document.get_outlines()
	for (level,title,dest,a,se) in outlines:
		print (level, title)

def getPages():
	for pageNumber, page in enumerate(PDFDocument.get_pages()):
		if pageNumber == 42:
        #do something with the page

def _parse_pages (doc):
	
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in doc.get_pages():
        interpreter.process_page(page)
        # receive the LTPage object for this page
        layout = device.get_result()
        # layout is an LTPage object which may contain child objects like LTTextBox, LTFigure, LTImage, etc.
	return layout