from sqlalchemy.orm import Session
from repository import (
    get_kingdom_list as db_get_kingdom_list,
    get_kingdom as db_get_kingdom,
    create_kingdom as db_create_kingdom,
    
    get_king_list as db_get_king_list,
    get_king as db_get_king,
    create_king as db_create_king,
    
    get_vizier_list as db_get_vizier_list,
    get_vizier as db_get_vizier,
    create_vizier as db_create_vizier,
    
    get_laymen_list as db_get_laymen_list,
    get_laymen as db_get_laymen,
    create_laymen as db_create_laymen
)

from schema import (
    CreateKingdom,
    GetKingdomList,
    GetKingdom, 
    
    CreateKing,
    GetKingList,
    GetKing,
    
    CreateVizier,
    GetVizierList, 
    GetVizier, 
    
    CreateLaymen, 
    GetLaymenList, 
    GetLaymen
)


async def get_kingdom_list(db: Session, skip: int, limit: int):
    response = db_get_kingdom_list(db = db, skip = skip, limit = limit)
    return response
    

async def get_kingdom(db: Session, id: int):
    response = db_get_kingdom(db = db, kingdom_id=id)
    return response
    
async def create_kingdom(db: Session, req: CreateKingdom):
    request = db_create_kingdom(db = db, req = req)
    return request 


async def get_king_list(db: Session, skip: int, limit: int):
    response = db_get_king_list(db = db, skip = skip, limit = limit)
    return response
    

async def get_king(db: Session, id: int):
    response = db_get_king(db = db, king_id=id)
    return response
    
    
async def create_king(db: Session, req: CreateKing):
    request = db_create_king(db = db, req = req)
    return request
    
    
async def get_vizier_list(db: Session, skip:int, limit: int):
    response = db_get_vizier_list(db = db, skip=skip, limit=limit)
    return response
    

async def get_vizier(db: Session, id: int):
    response = db_get_vizier(db = db, vizier_id = id)
    return response
    

async def create_vizier(db: Session, req: CreateVizier):
    request = db_create_vizier(db = db, req = req)
    return request
    
    
async def get_laymen_list(db: Session, skip:int, limit:int):
    response = db_get_laymen_list(db = db, skip=skip, limit=limit)
    return response
    

async def get_laymen(db: Session, id: int):
    response = db_get_laymen(db = db, laymen_id = id)
    return response
    

async def create_laymen(db: Session, req: create_laymen):
    request = db_create_laymen(db = db, req = req)
    return request