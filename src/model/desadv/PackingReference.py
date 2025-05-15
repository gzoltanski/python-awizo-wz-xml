from dataclasses import dataclass
from .base import DesadvBase

@dataclass
class PackingReference(DesadvBase):
    package_id: str
    package_number: str
    package_type: str
    serial_number: str