import xml.etree.ElementTree as ET
from .base import DesadvBase

class PackingReference(DesadvBase):
    def __init__(self, desadv_file: str) -> None:
        super().__init__(desadv_file)
        self.node = self.desadv.find(".//Packing-Reference")

        self.package_i_d = self.node.findtext("PackageID")
        self.package_number = self.node.findtext("PackageNumber")
        self.package_type = self.node.findtext("PackageType")
        self.serial_number = self.node.findtext("SerialNumber")

    def get_package_i_d(self) -> str | None:
        return self.package_i_d

    def get_package_number(self) -> str | None:
        return self.package_number

    def get_package_type(self) -> str | None:
        return self.package_type

    def get_serial_number(self) -> str | None:
        return self.serial_number

    def set_package_i_d(self, value: str | None) -> None:
        self._set_xml_text("PackageID", value)

    def set_package_number(self, value: str | None) -> None:
        self._set_xml_text("PackageNumber", value)

    def set_package_type(self, value: str | None) -> None:
        self._set_xml_text("PackageType", value)

    def set_serial_number(self, value: str | None) -> None:
        self._set_xml_text("SerialNumber", value)

    def _set_xml_text(self, tag: str, value: str | None) -> None:
        elem = self.node.find(tag)
        if elem is None:
            elem = ET.SubElement(self.node, tag)
        elem.text = "" if value is None else str(value)