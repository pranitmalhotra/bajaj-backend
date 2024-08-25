from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Request(BaseModel):
    data: List[str]

class Response(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    numbers: List[str]
    alphabets: List[str]
    highest_lowercase_alphabet: List[str]

@app.get("/bfhl")
async def get_bfhl():
    return {"operation_code": 1}

@app.post("/bfhl")
async def post_bfhl(request: Request):
    numbers = []
    alphabets = []
    
    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        elif len(item) == 1 and item.isalpha():
            alphabets.append(item)
    
    highest_lowercase = max((c for c in alphabets if c.islower()), default=None)
    highest_lowercase_alphabet = [highest_lowercase] if highest_lowercase else []

    return Response(
        is_success=True,
        user_id="john_doe_17091999",
        email="john@xyz.com",
        roll_number="ABCD123",
        numbers=numbers,
        alphabets=alphabets,
        highest_lowercase_alphabet=highest_lowercase_alphabet
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)