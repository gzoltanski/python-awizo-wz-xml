from dataclasses import dataclass

@dataclass
class PackingReference:
    package_id: str
    package_number: str
    package_type: str
    serial_number: str
