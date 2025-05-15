from dataclasses import dataclass
from src.model.self.desadv.Range import Range
from .base import DesadvBase

@dataclass
class GoodsIdentity(DesadvBase):
    type: str
    range: Range