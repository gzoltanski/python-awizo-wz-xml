from dataclasses import dataclass
from src.model.desadv.GoodsIdentity import GoodsIdentity

@dataclass
class PackageIdentification:
    goods_identity: GoodsIdentity