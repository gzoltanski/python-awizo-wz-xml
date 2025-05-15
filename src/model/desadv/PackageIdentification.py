from dataclasses import dataclass
from src.model.self.desadv.GoodsIdentity import GoodsIdentity
from .base import DesadvBase

@dataclass
class PackageIdentification(DesadvBase):
    goods_identity: GoodsIdentity