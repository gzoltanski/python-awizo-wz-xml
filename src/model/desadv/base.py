from . import XmlDocument

class DesadvBase:
    """Wspólna funkcjonalność dla wszystkich obiektów DESADV."""
    def __init__(self, desadv_file: str) -> None:
        # Jednorazowa inicjalizacja parsera XML
        self.desadv = XmlDocument(desadv_file)