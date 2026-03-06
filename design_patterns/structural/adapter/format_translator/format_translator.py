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

