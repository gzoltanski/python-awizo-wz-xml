from src.model import *
from pathlib import Path
import xml.etree.ElementTree as ET

class XmlDocument():
    """Klasa-szablon dla dokumentów XML"""
    def __init__(self, xml_file: Path) -> None:
        self.xml_file = xml_file
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()

    def __repr__(self):
        return f"{ET.dump(self.root)}"

    def display(self):
        ET.dump(self.root)

class DesadvBase:
    """Klasa bazowa dla wszystkich obiektów DESADV."""

    def __init__(self, desadv_file: Path) -> None:
        # Jednorazowa inicjalizacja parsera XML
        self.desadv = XmlDocument(desadv_file)