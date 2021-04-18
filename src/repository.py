from sqlalchemy.orm import Session

import model, schema

def get_kingdom(db: Session, kingdom_id: int):
    return db.query(model.Kingdom).filter(model.Kingdom.id == kingdom_id).first()

def get_kingdom_list(db: Session, skip:int = 0, limit:int = 100):
    return db.query(model.Kingdom).offset(skip).limit(limit).all()

def create_kingdom(db: Session, req: schema.CreateKingdom):
    object_req = model.Kingdom(**req.dict())
    db.add(object_req)
    db.commit()
    db.refresh(object_req)
    return object_req


def get_king(db: Session, king_id: int):
    return db.query(model.King).filter(model.King.id == king_id).first()

def get_king_list(db: Session, skip:int = 0, limit:int = 100):
    return db.query(model.King).offset(skip).limit(limit).all()

def create_king(db: Session, req: schema.CreateKing):
    object_req = model.King(**req.dict())
    db.add(object_req)
    db.commit()
    db.refresh(object_req)
    return object_req

def get_vizier(db: Session, vizier_id: int):
    return db.query(model.Vizier).filter(model.Vizier.id == vizier_id).first()

def get_vizier_list(db: Session, skip:int = 0, limit:int = 100):
    return db.query(model.Vizier).offset(skip).limit(limit).all()

def create_vizier(db: Session, req: schema.CreateVizier):
    object_req = model.Vizier(**req.dict())
    db.add(object_req)
    db.commit()
    db.refresh(object_req)
    return object_req


def get_laymen(db: Session, laymen_id: int):
    return db.query(model.Laymen).filter(model.Laymen.id == laymen_id).first()

def get_laymen_list(db: Session, skip:int = 0, limit:int = 100):
    return db.query(model.Laymen).offset(skip).limit(limit).all()

def create_laymen(db: Session, req: schema.CreateLaymen):
    object_req = model.Laymen(**req.dict())
    db.add(object_req)
    db.commit()
    db.refresh(object_req)
    return object_req
