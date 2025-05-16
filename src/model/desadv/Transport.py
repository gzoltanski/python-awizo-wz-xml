from . import *

class Transport(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node='DespatchAdvice-Transport'):
        super().__init__(desadv_file,
                         node,
                         terms_of_delivery='TermsOfDelivery',
                         conveyance_reference_number='ConveyanceReferenceNumber',
                         mode_of_transport='ModeOfTransport'
                         )
