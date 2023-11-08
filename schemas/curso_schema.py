from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

#Como o SQL Alchemy tem o BaseModel dele, não poderemos confundir...

class CursoSchemas(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    instutor: str
    class Config:
        from_attributes = True