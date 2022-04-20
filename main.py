import pyttsx3
import PyPDF2

book = open("Cloud_Computing_Assignment_2.pdf", 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speak = pyttsx3.init()
page = pdfreader.getPage(0)
text = page.extractText()
speak.say(text)
speak.runAndWait()
