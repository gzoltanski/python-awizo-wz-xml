from src.model.self.desadv.Header import Header
from src.model.self.desadv.Transport import Transport
from src.model.self.desadv.Parties import Parties
from src.model.self.desadv.Consignment import Consigment
from .base import DesadvBase


class DespatchAdvice(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.despatchadvice = self.desadv.root.find(f'.//DespatchAdvice')
        self.header = self.despatchadvice.find('./Header') or self.despatchadvice.find('./HEADER')
        self.transport = self.despatchadvice.find('./Transport') or self.despatchadvice.find('./TRANSPORT')
        self.parties = self.despatchadvice.find('./Parties') or self.despatchadvice.find('./PARTIES')
        self.consigment = self.despatchadvice.find('./Consigment') or self.despatchadvice.find('./CONSIGMENT')
    header: Header
    transport: Transport
    parties: Parties
    consigment: Consigment