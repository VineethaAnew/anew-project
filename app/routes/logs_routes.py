from fastapi import APIRouter

# Create router instance
router = APIRouter()

# Example endpoint
@router.get("/logs")
def get_logs():
    return {"message": "Logs router works!"}
