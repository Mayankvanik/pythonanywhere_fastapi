from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/hello")
async def read_hello():
    return {"message": "hello guys"}

if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=6000, reload=True)