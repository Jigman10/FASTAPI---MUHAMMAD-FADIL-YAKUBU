from pydantic import BaseModel,validator
from fastapi  import HTTPException,status

class Todo(BaseModel):
    title:str
    description:str
    priority:int=0


    @validator('priority')
    def validate_priority(cls,value):
        if not value in [0,1,2]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Priority must be 0(Low), 1(Mid) or 2(High)")
            
        
        return value

