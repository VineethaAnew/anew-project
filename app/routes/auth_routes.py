from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# Create the router
router = APIRouter()

# Example Pydantic model for login
class LoginRequest(BaseModel):
    username: str
    password: str

# Example route
@router.post("/login")
def login(request: LoginRequest):
    # Placeholder logic
    if request.username == "admin" and request.password == "password":
        return {"message": "Login successful!"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )

# Another example route
@router.get("/status")
def status():
    return {"message": "Auth router is working!"}
