# log-decorator

Um decorador de logging flexível e poderoso para Python, construído sobre o Loguru.

Criado por [Bruno Sardou](https://github.com/bruno-sardou)

## Características

- Decorador de funções para logging automático
- Filtragem hierárquica de níveis de log
- Exibição colorida no console
- Criação automática de diretórios de log
- Registro em arquivo e console simultaneamente
- Informações de contexto (usuário, arquivo)
- Uso flexível (com ou sem parênteses)

## Instalação

```bash
pip install log-decorator
```

Ou com Poetry:

```bash
poetry add log-decorator
```

## Uso Básico

```python
from log_decorator import log_decorator

# Uso básico (nível INFO padrão)
@log_decorator
def soma(a, b):
    return a + b

# Especificando um nível
@log_decorator(level="DEBUG")
def multiplica(a, b):
    return a * b

# Função que gera erro
@log_decorator(level="ERROR")
def divide(a, b):
    return a / b

# Usando as funções
soma(5, 3)       # Registra chamada e resultado no nível INFO
multiplica(4, 2)  # Registra chamada e resultado no nível DEBUG
divide(10, 0)     # Registra erro no nível ERROR
```

## Níveis Disponíveis

- TRACE (5)
- DEBUG (10)
- INFO (20)
- SUCCESS (25)
- WARNING (30)
- ERROR (40)
- CRITICAL (50)

## Saída de Log

No console (colorido):
```
INFO | Executando 'soma' com args=(5, 3), kwargs={}
SUCCESS | Resultado de 'soma': 8
```

No arquivo de log (pasta `logs/` no diretório do projeto):
```
2025-03-01T14:23:45.123456 | INFO | Executando 'soma' com args=(5, 3), kwargs={} | Usuário: joao | Arquivo: exemplo.py
2025-03-01T14:23:45.123498 | SUCCESS | Resultado de 'soma': 8 | Usuário: joao | Arquivo: exemplo.py
```

## Licença

MIT