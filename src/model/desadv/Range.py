from dataclasses import dataclass
from .base import DesadvBase

@dataclass
class Range(DesadvBase):
    id_begin: str