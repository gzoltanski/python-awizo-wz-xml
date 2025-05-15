from dataclasses import dataclass
from src.model.self.desadv.Header import Header
from src.model.self.desadv.Transport import Transport
from src.model.self.desadv.Parties import Parties
from src.model.self.desadv.Consignment import Consigment
from .base import DesadvBase


@dataclass
class DespatchAdvice(DesadvBase):
    header: Header
    transport: Transport
    parties: Parties
    consigment: Consigment