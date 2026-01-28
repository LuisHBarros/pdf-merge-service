from fastapi import FastAPI
from app.api.routes import pdf

app = FastAPI(
    title="PDF Merger Microservice",
    version="1.0.0",
    description="Microserviço para mesclar PDFs"
)

app.include_router(pdf.router)


@app.get("/health", tags=["Infra"])
def health_check():
    return {"status": "ok"}
