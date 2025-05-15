from dataclasses import dataclass
from src.model.self.desadv.PackingReference import PackingReference
from src.model.self.desadv.Line import Line
from .base import DesadvBase

@dataclass
class PackingSequence(DesadvBase):
    packing_reference: PackingReference
    line: Line