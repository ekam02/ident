# Ident

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
