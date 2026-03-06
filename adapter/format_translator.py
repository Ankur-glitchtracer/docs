# Adapter Design Pattern

# The "Format Translator"
# Target (What your app wants): A class JsonParser with a method request_json().

# Adaptee (The incompatible 3rd party): A class XmlAnalytics that has a method get_xml_data().

# Adapter: A class that inherits from (or wraps) JsonParser but internally calls XmlAnalytics and "converts" the data.

# How would you structure the Adapter so your app thinks it's just talking to a regular JSON parser?


class JsonParser:
    def request_json(self) -> str:
        return "Converting the json data..."


class XmlAnalytics:
    def get_xml_data(self) -> str:
        return "Converting the xml data..."


class Adapter(JsonParser):
    def __init__(self, xml: XmlAnalytics) -> None:
        self.xml : XmlAnalytics = xml

    def request_json(self) -> str:
        xml_data = self.xml.get_xml_data()
        return f"{xml_data} -> Converted to JSON"

xml = XmlAnalytics()

adapter = Adapter(xml=xml)

print(adapter.request_json())

