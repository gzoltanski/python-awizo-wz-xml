from .base import DesadvBase


class Transport(DesadvBase):
    def __init__(self, desadv_file: Path):
        super().__init__(desadv_file)
        self.transport = self.desadv.root.find(f'.//Transport')
        self.terms_of_delivery = self.transport.find('./TermsOfDelivery') or self.transport.find('./TERMS_OF_DELIVERY')
        self.conveyance_reference_number = self.transport.find('./ConveyanceReferenceNumber') or self.transport.find('./CONVEYANCE_REFERENCE_NUMBER')
        self.mode_of_transport = self.transport.find('./ModeOfTransport') or self.transport.find('./MODE_OF_TRANSPORT')
    terms_of_delivery: str
    conveyance_reference_number: str
    mode_of_transport: str