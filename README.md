## PDF Merger Microservice

Microserviço em Python/FastAPI para **mesclar múltiplos arquivos PDF** em um único PDF.

### Tecnologias

- **Python 3.11**
- **FastAPI** + **Uvicorn**
- **pypdf** para manipulação de PDFs
- **pytest** para testes automatizados

### Estrutura do projeto

- `app/main.py` – criação da aplicação FastAPI e rota `/health`
- `app/api/routes/pdf.py` – rota `/pdf/merge` para upload e merge de PDFs
- `app/services/pdf_service.py` – lógica de mesclagem de PDFs
- `app/tests/` – testes automatizados (incluindo arquivos PDF de exemplo)

### Configuração do ambiente

1. Crie e ative o virtualenv (se ainda não existir):

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando o servidor

Na raiz do projeto:

```bash
venv\Scripts\activate
uvicorn app.main:app --reload
```

Por padrão, o serviço ficará disponível em:

- Documentação interativa: `http://127.0.0.1:8000/docs`
- Health check: `GET http://127.0.0.1:8000/health`

### Endpoint de merge de PDFs

- **URL**: `POST /pdf/merge`
- **Content-Type**: `multipart/form-data`
- **Campo**: `files` (múltiplos arquivos)
- **Resposta**: um único arquivo `application/pdf` com todos os PDFs concatenados.

Regras de validação:

- É necessário enviar **pelo menos 2 arquivos**.
- Apenas PDFs válidos são aceitos; arquivos inválidos geram erro `400`.

### Executando os testes

Com o virtualenv ativo, na raiz do projeto:

```bash
pytest
```

Os testes cobrem:

- Health check (`/health`)
- Merge bem-sucedido de 2 PDFs
- Erro ao enviar menos de 2 arquivos
- Erro ao enviar arquivo inválido (não-PDF)

