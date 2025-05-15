from dataclasses import dataclass
from .base import DesadvBase

@dataclass

class Transport(DesadvBase):
    terms_of_delivery: str
    conveyance_reference_number: str
    mode_of_transport: str