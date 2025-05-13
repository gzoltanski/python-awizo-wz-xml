from dataclasses import dataclass
from src.model.desadv.PackingSequence import PackingSequence

@dataclass
class Consignment:
    packing_sequence: PackingSequence