from src.model import *
from pathlib import Path
from typing import TypeVar, Generic
import xml.etree.ElementTree as ET

T = TypeVar('T')

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
class Element(Generic[T]):
    def __init__(self, tag: str, parent_tag: str) -> None:
        self.tag = tag
        self.parent_tag = parent_tag
        self.children_tag = []






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


