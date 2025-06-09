# Buscador de Precatórios

Este projeto facilita a busca, consulta e gerenciamento de precatórios judiciais.

## Estrutura

```
buscador-de-precatorio/
├── backend/
│   └── main.py
├── scraping/
│   └── web_scraping.py
├── frontend/
│   └── nativo/
│       └── aplicacao_nativa.py
├── tests/
│   └── test_backend.py
└── README.md
```

## Execução

### Backend (API)
```bash
cd backend
uvicorn main:app --reload
```

### Scraping
```bash
cd scraping
uvicorn web_scraping:app --reload --port 8001
```

### Frontend nativo
```bash
cd frontend/nativo
python aplicacao_nativa.py
```

## Testes

Execute:
```bash
pytest tests/
```

## Exemplo de uso da API

- **Buscar precatórios:**  
  `GET http://localhost:8001/api/precatorios?cpf_cnpj=12345678900`
  Retorno esperado:  
  ```json
  {
    "trf3": [...],
    "trf1": [...]
  }
  ```

## Contribuição

1. Fork, branch, commit, push, pull request!
2. Veja a estrutura de diretórios padronizada.

## Licença

MIT