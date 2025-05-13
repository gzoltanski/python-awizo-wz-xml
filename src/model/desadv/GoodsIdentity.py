from dataclasses import dataclass
from src.model.desadv.Range import Range

@dataclass
class GoodsIdentity:
    type: str
    range: Range