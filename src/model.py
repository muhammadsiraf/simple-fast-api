from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Mankind(Base):
    __tablename__  = "mankinds"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    race = Column(String)
    
class Kingdom(Base):
    __tablename__ = "kingdoms"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    king = relationship("King", back_populates="kingdom")
    laymens = relationship("Laymen", back_populates="kingdom")
    
class King(Mankind):
    __tablename__ = "kings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    kingdom = Column(ForeignKey("kingdoms.id"))
    viziers = relationship("Vizier", back_populates="king")
    
class Vizier(Mankind):
    __tablename__ = "viziers"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    king_id = Column(ForeignKey("kings.id"))
    king = relationship("King", back_populates="viziers")
    
class Laymen(Mankind):
    __tablename__ = "laymens"
    
    id = Column(Integer, primary_key=True, index=True)
    kingdom_id = Column(ForeignKey("kingdoms.id"))
    kingdom = relationship("Kingdom", back_populates="laymens")
        