from fastapi import FastAPI
from routers import auth, users, products
app = FastAPI(root_path='/api')

app.title = "FastAPI API"
app.description = "FastAPI API"
app.version = "0.0.1"

app.include_router(users.router)
app.include_router(products.router)
app.include_router(auth.router)

@app.get("/",)
async def getMessage():
  return { "message":"Hello world Diego Alzate" }
 

@app.get("/url")
async def getUrl():
  return { "url":"https://www.gihub.com/dfalzate"}

