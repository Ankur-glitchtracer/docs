# The Template Method is a behavioral design pattern that defines the skeleton of an algorithm
# in a base class but lets subclasses override specific steps of the algorithm without changing its overall structure.

# Think of it like a recipe: The "Master Chef" (Base Class) decides the order of steps (boil water, add ingredients, garnish),
# but the "Sous Chef" (Subclass) decides what ingredients are added.

# The Challenge: Data Export Tool
# Imagine you are building a tool that exports data from a database into different formats (CSV and PDF).
# Both export processes follow the same high-level sequence, but the internal details differ.

# The Problem Statement
# You need to implement a system where:

# All exports must follow this exact sequence: Read Data -> Format Data -> Write to File.
# The Read Data step is always the same (fetching from a mock database).
# The Format Data and Write to File steps vary depending on the format.

# Implementation Template
# To get you started without giving away the full logic, here is the skeleton:

# Python
# from abc import ABC, abstractmethod

# class DataExporter(ABC):
#     # This is the "Template Method"
#     def export(self):
#         self._read_data()
#         self._format_data()
#         self._write_file()

#     def _read_data(self):
#         # Shared logic: everyone reads from the same DB
#         print("Reading data from SQL Database...")

#     @abstractmethod
#     def _format_data(self):
#         # Subclasses must implement this
#         pass

#     @abstractmethod
#     def _write_file(self):
#         # Subclasses must implement this
#         pass

# # Now, you create CSVExporter and PDFExporter...
# Why this is useful
# Code Reuse: You don't rewrite the database reading logic for every new format.

# Inversion of Control: This is often called the "Hollywood Principle": Don't call us, we'll call you.
# The base class calls the subclass methods, not the other way around.

# Your Task
# Implement a CSVExporter that formats data as comma-separated values.

# Implement a PDFExporter that formats data with "PDF Header/Footer" tags.

# Bonus: Add a "Hook." A hook is an optional method in the base class that does nothing by default but can be overridden
# (e.g., _send_notification() after the file is written).

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

