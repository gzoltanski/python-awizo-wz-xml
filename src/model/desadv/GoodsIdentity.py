from src.model.self.desadv.Range import Range
from .base import DesadvBase

class GoodsIdentity(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.goodsidentity = self.desadv.root.find(f'.//GoodsIdentity')
        self.type = self.goodsidentity.find('./Type') or self.goodsidentity.find('./TYPE')
        self.range = self.goodsidentity.find('./Range') or self.goodsidentity.find('./RANGE')
    type: str
    range: Range