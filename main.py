from fastapi import FastAPI

app = FastAPI()


#Path Operation or the Route

@app.get("/")
async def root():
    return {"message": "Welcome to my api !!!!"}

@app.get("/posts")
def get_posts():
    return {"message": "These are your posts"}