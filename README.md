# Ident

Genera identificadores únicos alfanuméricos. Puede usarse como **biblioteca** o como **CLI**.

## Instalación

```bash
pip install -e .
```

Para desarrollo (pruebas y linters):

```bash
pip install -e ".[dev]"
```

## Uso como CLI

Tras instalar el paquete, el comando `ident` queda disponible:

```bash
ident
ident --amount 5
ident -a 3 -l 6 --alphabet 0123456789abcdef
```

| Opción | Descripción |
| --- | --- |
| `-a`, `--amount` | Cantidad de identificadores a imprimir (por defecto: `1`) |
| `-l`, `--length` | Longitud de cada secuencia (por defecto: `8`) |
| `--alphabet` | Alfabeto a usar (por defecto: dígitos y minúsculas) |

## Uso como biblioteca

```python
from ident import Ident
```

Use `Ident()` para crear identificadores únicos para sus tarjetas Anki; créelos sin la necesidad de entregar
argumentos de entrada.

Al no especificar argumentos de entrada, el programa asignará como longitud (`length`) el valor *8*;
asimismo, asignará como abecedario (`alphabet`) la cadena de caracteres *'0123456789abcdefghijklmnopqrstuvwxyz'*.

Si desea definir la longitud y/o el abecedario usado por el programa, especifíquelos al momento de crear la
instancia:

```python
random_colors = Ident(length=6, alphabet='0123456789abcdef')
```

Si desea redefinir alguno de los valores asignados a los atributos, bastaría con asignárselos directamente y seguir
usando el programa.

```python
token = Ident()                      # length == 8 and alphabet == Ident.ALPHABET
token.alphabet = '0123456789abcdef'  # alphabet == '0123456789abcdef'
token.length = 6                     # length == 6
```

También puede generar identificadores con el método de instancia o el estático:

```python
Ident.id()                 # una secuencia de longitud 8
Ident().identifier(3)      # lista con 3 secuencias
```

## Desarrollo

```bash
pytest
ruff check src tests
mypy src tests
```
