from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from typing import List

from app.services.pdf_service import merge_pdfs

router = APIRouter(prefix="/pdf", tags=["PDF Operations"])


@router.post(
    "/merge",
    summary="Mesclar PDFs",
    description="Recebe múltiplos PDFs e retorna um único arquivo concatenado."
)
async def merge(files: List[UploadFile] = File(...)):
    merged_pdf = await merge_pdfs(files)

    return StreamingResponse(
        merged_pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=merged.pdf"
        }
    )
