from src.model import *
from pathlib import Path
from typing import TypeVar, Generic
import xml.etree.ElementTree as ET



class XmlDocument:
    """Klasa-szablon dla dokumentów XML"""

    def __init__(self, xml_file: Path) -> None:
        self.xml_file = xml_file
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def __repr__(self):
        return f"{ET.dump(self.root)}"

    def add_element(self, parent, element, level):
        ET.SubElement(parent, element)
        ET.indent(parent, 2*" ", level=level)


# -------------------------------------------------------------------
class Element:
    def __init__(self, parent) -> None:
        self.parent = parent




class DesadvBase(XmlDocument):
    """Klasa bazowa dla wszystkich obiektów DESADV."""

    def __init__(self, xml_file: Path) -> None:
        super().__init__(xml_file)
        for child in self.root:
            setattr(self, child.tag.lower().split("-")[1], child)

    def clear_consignment(self):
        self.consignment.clear()

    def add_packing_sequence(self):
        self.add_element(self.consignment, "Packing-Sequence", 7)


