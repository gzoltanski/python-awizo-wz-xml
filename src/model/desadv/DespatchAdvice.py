from . import *

class DespatchAdvice(DesadvBase):
    def __init__(self,
                 desadv_file: Path,
                 node=None
                 ):
        super().__init__(
            desadv_file,
            node,
            header='DespatchAdvice-Header',
            transport='DespatchAdvice-Transport',
            parties='DespatchAdvice-Parties',
            consignment='DespatchAdvice-Consignment'
        )

    # def clear_consignment(self):
    #     # usunięcie wszystkich podelementów gałęzi "DespatchAdvice-Consigment"
    #     self.consignment.clear()
    #
    # def get_list_of_consigment(self):
    #         return list(self.consignment)
