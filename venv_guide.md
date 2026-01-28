# Criar ambiente virtual

python -m venv venv

# Ativar ambiente (Windows)

venv\Scripts\activate

# Ativar ambiente (Linux/Mac)

source venv/bin/activate

# Instalar dependências

pip install -r requirements.txt
uvicorn app.main:app --reload