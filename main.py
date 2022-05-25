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
    core = Core()
    return core


@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")

