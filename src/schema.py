from typing import List, Optional

from pydantic import BaseModel

# Mankind
class Mankind(BaseModel):
    name: str
    sex: str
    age: int
    race: str

    class Config:
        orm_mode = True

# Kingdom
class CreateKingdom(BaseModel):
    name: str

class GetKingdom(BaseModel):
    id: int
    name: str
    king: King
    laymens: List[Laymen] = []
    
    class Config:
        orm_mode = True
    
class GetKingdomList(BaseModel):
    kindoms: List[GetKingdom] = []
    
    
# King
class King(Mankind):
    title: str
    kingdom: int
    
    class Config:
        orm_mode = True

class CreateKing(King):
    pass

class GetKing(King):
    viziers: List[Vizier] = []
    
class GetKingList(BaseModel):
    kings: List[GetKing] = []
    
# Vizier
class Vizier(Mankind):
    title: str
    king_id: int
    
    class Config:
        orm_mode = True
    
class CreateVizier(Vizier):
    pass

class GetVizier(Vizier):
    pass

class GetVizierList(BaseModel):
    viziers: List[Vizier] = []

# Laymen
class Laymen(Mankind):
    kingdom_id: int
    
    class Config:
        orm_mode = True
    
class CreateLaymen(Laymen):
    pass

class GetLaymen(Laymen):
    pass

class GetLaymenList(BaseModel):
    laymens: List[Laymen] = []