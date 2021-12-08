from fastapi import FastAPI,status,HTTPException
from schema.todo import Todo
from fastapi.responses import JSONResponse



app = FastAPI()


todo_list =[]

@app.get("/api/v1/todos")
async def get_all():
 return {"Data":todo_list}

@app.post("/api/v1/todos")
async def create(todo:Todo):
    todo_list.append(todo.dict())
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content ={"Message":"Todo created succesfully","Data":todo.dict()}
    )