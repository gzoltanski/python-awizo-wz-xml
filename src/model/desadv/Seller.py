from src.model.desadv import *
from .base import DesadvBase

@dataclass
class Seller(DesadvBase):
    iln: str
    code_by_buyer: str