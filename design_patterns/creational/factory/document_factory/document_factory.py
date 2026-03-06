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

