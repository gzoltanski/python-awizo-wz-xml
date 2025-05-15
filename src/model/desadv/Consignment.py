from dataclasses import dataclass
from src.model.self.desadv.PackingSequence import PackingSequence
from .base import DesadvBase

@dataclass
class Consignment(DesadvBase):
    packing_sequence: PackingSequence