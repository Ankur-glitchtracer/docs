from abc import ABC, abstractmethod

class Exporter(ABC):

    def _read_data(self) -> dict:
        return {"key": "value"}

    @abstractmethod
    def _format_data(self, data: dict) -> str:
        pass

    @abstractmethod
    def _write_to_file(self, formatted: str) -> None:
        pass

    def _send_notification(self) -> None:
        pass

    def export(self):
        data = self._read_data()
        formatted = self._format_data(data)
        self._write_to_file(formatted=formatted)
        self._send_notification()


class CSVExporter(Exporter):
    def _format_data(self, data: dict) -> str:
        format_data: str = ""
        for key in data:
            format_data += f"{key},{data[key]}\n"

        return format_data

    def _write_to_file(self, formatted: str) -> None:
        print(f"{formatted}.csv")

    def _send_notification(self) -> None:
        print("Exported as CSV!")


class PDFExporter(Exporter):
    def _format_data(self, data: dict) -> str:
        format_data: str = "HEADER\n"
        for key in data:
            format_data += f"{key} {data[key]}\n"
        format_data += "FOOTER"

        return format_data

    def _write_to_file(self, formatted: str) -> None:
        print(f"{formatted}.pdf")

    def _send_notification(self) -> None:
        print("Exported as PDF!")


pdf_export = PDFExporter()
pdf_export.export()

csv_export = CSVExporter()
csv_export.export()

