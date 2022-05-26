from typing import List, Dict, Optional
from pydantic import Field
from .basemodels import ExtendedModel


class Core(ExtendedModel):
    pdb_code : str = Field(
        default=None, title="The PDB code of the structure", max_length=4
    )
    allele : Optional[str]
            