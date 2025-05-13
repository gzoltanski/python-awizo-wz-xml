from dataclasses import dataclass
from src.model.desadv.Header import Header
from src.model.desadv.Transport import Transport
from src.model.desadv.Parties import Parties
from src.model.desadv.Consignment import Consigment


@dataclass
class DespatchAdvice:
    header: Header
    transport: Transport
    parties: Parties
    consigment: Consigment
