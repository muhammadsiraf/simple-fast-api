# Hey this is main py file where all other modules are connected together and run from here

from fastapi import Depends, FastAPI

from router import mainRouter

app = FastAPI()

app.include_router(mainRouter)

@app.get("/")
async def root():
    return{
        "Message":"This is API Route"
    }