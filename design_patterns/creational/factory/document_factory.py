# The Factory Method Pattern
# The Problem: You are building a Document Management System. Your system needs to support different types of documents: PDFDocument and WordDocument.

# Every document has a name and a method open().

# You have a DocumentCreator class (the application itself).

# The Conflict: The application doesn't know ahead of time if the user wants to create a PDF or a Word doc. 
# If you use if type == "pdf": doc = PDFDocument(), your code becomes tightly coupled and hard to extend if you want to add ExcelDocument later.

# Your Goal:

# Create an abstract Document class.

# Create concrete PDFDocument and WordDocument classes.

# Create an abstract Application class with a method createDocument(). This is your Factory Method.

# Create PDFApplication and WordApplication that override createDocument() to return the specific type.

from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        pass


class PDFDocument(Document):
    def open(self) -> str:
        return "Opening the PDF..."

class WordDocument(Document):
    def open(self) -> str:
        return "Opening the Word"


class Application(ABC):
    @abstractmethod
    def factory_method(self) -> Document:
        pass

    def createDocument(self) -> str:
        product = self.factory_method()
        return product.open()


class PDFApplication(Application):
    def factory_method(self) -> Document:
        return PDFDocument()


class WordApplication(Application):
    def factory_method(self) -> Document:
        return WordDocument()

pdf = PDFApplication()
print(pdf.createDocument())

