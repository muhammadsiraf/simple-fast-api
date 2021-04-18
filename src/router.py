from fastapi import APIRouter


mainRouter = APIRouter()

@mainRouter.get("/kingdom/", tags=["kingdom"])
async def get_kingdom_list():
    return{
        "message":"this is kingdom list"
    }
    

@mainRouter.get("/kingdom/{id}", tags=["kingdom"])
async def get_kingdom(id: int):
    return{
        "message":"this is kingdom by id"
    }
    

@mainRouter.post("/kingdom/", tags=["kingdom"])
async def create_kingdom(name: str,):
    return{
        "message":f"created kingdom {name}"
    }
    
    


@mainRouter.get("/king/", tags=["king"])
async def get_king_list():
    return{
        "message":"this is king list"
    }
    

@mainRouter.get("/king/{id}", tags=["king"])
async def get_king(id: int):
    return{
        "message":"this is king by id"
    }
    

@mainRouter.post("/king/", tags=["king"])
async def create_king(name: str):
    return{
        "message":f"created king name {name}"
    }
    
    
    

@mainRouter.get("/vizier/", tags=["vizier"])
async def get_vizier_list():
    return{
        "message":"this is vizier list"
    }
    

@mainRouter.get("/vizier/{id}", tags=["vizier"])
async def get_vizier(id: int):
    return{
        "message":"this is vizier by id"
    }
    

@mainRouter.get("/vizier/", tags=["vizier"])
async def create_vizier(name: str):
    return{
        "message":f"created vizier name {name}"
    }
    
    

@mainRouter.get("/laymen/", tags=["laymen"])
async def get_laymen_list():
    return{
        "message":"this is laymen list"
    }
    

@mainRouter.get("/laymen/{id}", tags=["laymen"])
async def get_laymen(id: int):
    return{
        "message":"this is laymen by id"
    }
    

@mainRouter.get("/laymen/", tags=["laymen"])
async def create_laymen(name: str):
    return{
        "message":f"created laymen name {name}"
    }