from src.model.self.desadv.GoodsIdentity import GoodsIdentity
from .base import DesadvBase

class PackageIdentification(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.packageidentification = self.desadv.root.find(f'.//PackageIdentification')
        self.goods_identity = self.packageidentification.find('./GoodsIdentity') or self.packageidentification.find('./GOODS_IDENTITY')
    goods_identity: GoodsIdentity