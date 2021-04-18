from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import model
from database import SessionLocal, engine

from handler import (
    create_kingdom as hand_create_kingdom, 
    create_king as hand_create_king,
    create_vizier as hand_create_vizier,
    create_laymen as hand_create_laymen,
    
    get_kingdom as hand_get_kingdom, 
    get_king as hand_get_king,
    get_vizier as hand_get_vizier,
    get_laymen as hand_get_laymen,
    
    get_kingdom_list as hand_get_kingdom_list,
    get_king_list as hand_get_king_list,
    get_vizier_list as hand_get_vizier_list,
    get_laymen_list as hand_get_laymen_list
)

from schema import (
    CreateKingdom,
    CreateKing,
    CreateVizier,
    CreateLaymen, 
    
    GetKingdom,
    GetKing,
    GetVizier,
    GetLaymen,
    
    GetKingdomList,
    GetKingList,
    GetVizierList,
    GetLaymenList
)

model.Base.metadata.create_all(bind=engine)

mainRouter = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


@mainRouter.get("/kingdom/", tags=["kingdom"], response_model = GetKingdomList)
async def get_kingdom_list(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    response = hand_get_kingdom_list(db = db, skip = skip, limit = limit)
    return response
    

@mainRouter.get("/kingdom/{id}", tags=["kingdom"], response_model = GetKingdom)
async def get_kingdom(id: int, db: Session = Depends(get_db)):
    response = hand_get_kingdom(db = db, id = id)
    return response
    

@mainRouter.post("/kingdom/", tags=["kingdom"])
async def create_kingdom(req: CreateKingdom, db: Session = Depends(get_db)):
    request = hand_create_kingdom(db = db, req = req)
    return request
    
    
@mainRouter.get("/king/", tags=["king"], response_model = GetKingList)
async def get_king_list(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    response = hand_get_king_list(db = db , skip=skip, limit = limit)
    return response
    

@mainRouter.get("/king/{id}", tags=["king"], response_model = GetKing)
async def get_king(id: int, db: Session = Depends(get_db)):
    response = hand_get_king(db = db, id = id)
    return response
    

@mainRouter.post("/king/", tags=["king"])
async def create_king(req: CreateKing, db: Session = Depends(get_db)):
    request = hand_create_king(db = db, req = req)
    return request
    
    
@mainRouter.get("/vizier/", tags=["vizier"], response_model = GetVizierList)
async def get_vizier_list(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    response = hand_get_vizier_list(db = db, skip=skip, limit=limit)
    return response
    

@mainRouter.get("/vizier/{id}", tags=["vizier"], response_model = GetVizier)
async def get_vizier(id: int, db: Session = Depends(get_db)):
    response = hand_get_vizier(db = db, id = id)
    return response
    

@mainRouter.get("/vizier/", tags=["vizier"])
async def create_vizier(req: CreateVizier, db: Session = Depends(get_db)):
    request = hand_create_vizier(db = db, req = req)
    return request
    
    
@mainRouter.get("/laymen/", tags=["laymen"], response_model = GetLaymenList)
async def get_laymen_list(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    response = hand_get_laymen_list(db = db, skip=skip, limit=limit)
    return response
    

@mainRouter.get("/laymen/{id}", tags=["laymen"], response_model = GetLaymen)
async def get_laymen(id: int, db: Session = Depends(get_db)):
    response = hand_get_laymen(db = db, id = id)
    return response
    

@mainRouter.get("/laymen/", tags=["laymen"])
async def create_laymen(req: CreateLaymen, db: Session = Depends(get_db)):
    request = hand_create_laymen(db = db, req = req)
    return request