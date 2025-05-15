from src.model import *
# from abc import ABC, abstractmethod
from pathlib import Path
import xml.etree.ElementTree as ET

class XmlDocument():
    def __init__(self, xml_doc: Path) -> None:
        self.xml_doc = xml_doc
        self.tree = ET.parse(self.xml_doc)
        self.root = self.tree.getroot()

    def __repr__(self):
        return f"{ET.dump(self.root)}"

    def display(self):
        ET.dump(self.root)

