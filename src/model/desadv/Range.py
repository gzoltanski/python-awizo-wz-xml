from .base import DesadvBase

class Range(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.range = self.desadv.root.find(f'.//Range')
        self.id_begin = self.range.find('./IdBegin') or self.range.find('./ID_BEGIN')
    id_begin: str