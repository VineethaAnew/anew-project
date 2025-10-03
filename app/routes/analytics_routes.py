from fastapi import APIRouter

# 1️⃣ Create router instance
router = APIRouter()

# 2️⃣ Add endpoints
@router.get("/")
def analytics_root():
    return {"message": "Analytics router works!"}
