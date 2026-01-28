import io
from typing import List

from fastapi import HTTPException, UploadFile
from pypdf import PdfReader, PdfWriter


async def merge_pdfs(files: List[UploadFile]) -> io.BytesIO:
    """
    Merge multiple uploaded PDF files into a single PDF.
    """
    if len(files) < 2:
        raise HTTPException(
            status_code=400,
            detail="Envie pelo menos 2 arquivos PDF.",
        )

    writer = PdfWriter()
    valid_files = 0

    for file in files:
        content = await file.read()

        try:
            reader = PdfReader(io.BytesIO(content))
            writer.append(reader)
            valid_files += 1
        except Exception:
            # Arquivo não pôde ser lido como PDF
            raise HTTPException(
                status_code=400,
                detail=f"O arquivo '{file.filename}' não é um PDF válido.",
            )

    if valid_files < 2:
        raise HTTPException(
            status_code=400,
            detail="É necessário pelo menos 2 PDFs válidos.",
        )

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)

    return output
