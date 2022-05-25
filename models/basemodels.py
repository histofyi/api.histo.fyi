from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from pydantic import ValidationError


class ConfigModel(BaseModel):
    pass
    #class Config:
    #    alias_generator = humps.camelize