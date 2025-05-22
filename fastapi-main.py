from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates #can use jinja to direct put var in html

from datetime import datetime
from pydantic import BaseModel, Field
import uuid
from typing import Dict

app = FastAPI(title= "ToDO List API")
app.mount("/static",app= StaticFiles(directory="static"), name="static folder")
templates = Jinja2Templates(directory="lab-material/templates")

#pydantic model to declare data type
class ToDoItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str | None = None  #can be none default or any string val
    due_at: datetime | None = None
    completed: bool  = False
    created_at: datetime = Field(default_factory=lambda: datetime.now())

todos :Dict[str, ToDoItem]={  #type str value todoitem
    "1" : ToDoItem (
        id="1",
        title="할 일 1",
        due_at= datetime(year=2025, month=6, day=20),
        description="my todo list"
    ),
    "2" : ToDoItem (
        id="2",
        title="할 일 2",
        due_at= datetime(year=2025, month=7, day=20),
        description="my todo list 2"
    )

} 
#can use url/docs to see fastapi documentation about our page

@app.get("/") #use uvicorn main:app to run
def get_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) #return html 

@app.get("/todos")  #return list default
def get_todos():
    return list(todos.values())

@app.patch("/todos/{item_id}/toogle") #patch update completed specific value
def toogle_todo_completion(item_id:str):
        if item_id not in todos:
             raise HTTPException("not found item todo")
        
        todo = todos[item_id]
        todo.completed = not todo.completed #to make false to true by make it opposite
        return todo

@app.delete("/todos/{item_id}")  #delete from list
def delete_item(item_id: str):
       if item_id not in todos:
             raise HTTPException("not found item todo")
       
       del todos[item_id]
       return {"message:" "todo item is deleted"}

@app.post("/todos")         # add to list
def create_todo(item: ToDoItem):
     todos[item.id] = item
     return item