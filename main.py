from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from fastapi_cache.backends.inmemory import InMemoryBackend

from datetime import datetime

from models import Core


app = FastAPI()



@app.get("/", response_model=Core)
#@cache(expire=5)
async def root():
    data = {'pdb_code':'1hhk','allele':'HLA-A*02:01:01:01'}
    core = Core(**data)
    return core


@app.get("/api/v1/structures/core/{pdb_code}", response_model=Core)
@cache(expire=5)
async def structures_core(pdb_code):
    data = {'pdb_code':pdb_code,'allele':'HLA-A*02:01:01:01'}
    core = Core(**data)
    return core








@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

