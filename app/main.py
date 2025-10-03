from fastapi import FastAPI
from app.routes import auth_routes, questionnaire_routes, logs_routes, analytics_routes

app = FastAPI(title="Anew Backend")

# Include Routers
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(questionnaire_routes.router, prefix="/questionnaire", tags=["questionnaire"])
app.include_router(logs_routes.router, prefix="/logs", tags=["logs"])
app.include_router(analytics_routes.router, prefix="/analytics", tags=["analytics"])

@app.get("/")
def root():
    return {"message": "Welcome to Anew API"}
