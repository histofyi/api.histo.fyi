from typing import List, Dict, Optional
from pydantic import Field
from .basemodels import ConfigModel


class Core(ConfigModel):
    pdb_code : Optional[str] = Field(
        default=None, title="The PDB code of the structure", max_length=32
    )
    name : Optional[str]