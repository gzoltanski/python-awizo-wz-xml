from dataclasses import dataclass
from src.model.desadv.PackingReference import PackingReference
from src.model.desadv.Line import Line

@dataclass
class PackingSequence:
    packing_reference: PackingReference
    line: Line