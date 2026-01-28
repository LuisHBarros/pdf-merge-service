from pathlib import Path

PDF_1 = Path(__file__).parent / "assets" / "000056810.pdf"
PDF_2 = Path(__file__).parent / "assets" / "000056896.pdf"
TXT_FILE = Path(__file__).parent / "assets" / "invalid.txt"


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_merge_success(client):
    with open(PDF_1, "rb") as f1, open(PDF_2, "rb") as f2:
        response = client.post(
            "/pdf/merge",
            files=[
                ("files", ("file1.pdf", f1, "application/pdf")),
                ("files", ("file2.pdf", f2, "application/pdf")),
            ]
        )

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content.startswith(b"%PDF")


def test_merge_less_than_two_files(client):
    with open(PDF_1, "rb") as f1:
        response = client.post(
            "/pdf/merge",
            files=[
                ("files", ("file1.pdf", f1, "application/pdf")),
            ]
        )

    assert response.status_code == 400
    assert "2 arquivos" in response.json()["detail"]


def test_merge_invalid_file(client):
    with open(PDF_1, "rb") as f1, open(TXT_FILE, "rb") as txt:
        response = client.post(
            "/pdf/merge",
            files=[
                ("files", ("file1.pdf", f1, "application/pdf")),
                ("files", ("invalid.txt", txt, "text/plain")),
            ]
        )

    assert response.status_code == 400
    assert "não é um PDF válido" in response.json()["detail"]
