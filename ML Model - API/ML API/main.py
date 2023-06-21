from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from utils.recommend import get_recommendationyelp

app = FastAPI()

origins = [
    
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Yelp Users Restaurant Recommendation API"}


@app.get("/restaurantes/recomendacion/{id_usuario}")
async def recomendacion_restaurantes(id_usuario):
    return get_recommendationyelp(id_usuario)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)