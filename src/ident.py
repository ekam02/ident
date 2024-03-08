import string
import random
import re


class Ident:
    ALPHABET = string.digits + string.ascii_lowercase

    @staticmethod
    def id() -> str:
        """Entrega un Ident alfanumérico de 8 caracteres de longitud"""
        return ''.join(random.choices(Ident.ALPHABET, k=8))

    @classmethod
    def is_positive_number(cls, number: int) -> bool:
        """Comprueba si ``number`` es un entero positivo"""
        result = False
        try:
            result = True if number >= 1 else False
        except TypeError:
            print(f"El argumento {number} debería ser tipo 'Numérico'.")
        finally:
            return result

    @classmethod
    def is_alphabet(cls, alphabet: str) -> bool:
        """Comprueba si ``alphabet`` es de tipo str"""
        result = False
        try:
            result = True if len(alphabet) > 1 and isinstance(alphabet, str) else False
        except TypeError:
            print(f"El argumento {alphabet} debería ser tipo 'Cadena de Caracteres'.")
        finally:
            return result

    @classmethod
    def normalize_length(cls, length: int) -> int:
        """Determina si ``length`` es adecuado o no para Ident"""
        return int(length) if cls.is_positive_number(length) else 8

    @classmethod
    def normalize_alphabet(cls, alphabet: str) -> str:
        """Determina si ``alphabet`` es adecuado o no para Ident"""
        def sort(sentence: list) -> list:
            """Organiza el contenido de ``sentence``"""
            sentence.sort()
            return sentence

        return ''.join(sort([character for character in set(alphabet) if not re.search(r'\s', character)])) if \
            cls.is_alphabet(alphabet) else cls.ALPHABET

    def __init__(self, *args, **kwargs) -> None:
        """Instancia un objeto Ident"""
        if args:
            self.__length = self.normalize_length(args[0]) if len(args) > 0 else 8
            self.__alphabet = self.normalize_alphabet(args[1]) if len(args) > 1 else self.ALPHABET
        elif kwargs:
            self.__length = self.normalize_length(kwargs['length']) if 'length' in kwargs else 8
            self.__alphabet = self.normalize_alphabet(kwargs['alphabet']) if 'alphabet' in kwargs else self.ALPHABET
        else:
            self.__length = 8
            self.__alphabet = self.ALPHABET

    @property
    def length(self) -> int:
        """Informa la longitud de la instancia"""
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        """Asigna una longitud para la instancia"""
        self.__length = self.normalize_length(length)

    @property
    def alphabet(self) -> str:
        """Informa el abecedario de la instancia"""
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet: str) -> None:
        """Asigna el abecedario para la instancia"""
        self.__alphabet = self.normalize_alphabet(alphabet)

    def identifier(self, amount: int = 1) -> list:
        """Entrega un listado de secuencias representativas a Ident"""
        amount = amount if self.is_positive_number(amount) else 1
        return [''.join(random.choices(self.__alphabet, k=self.__length)) for _ in range(amount)]
    
    def __repr__(self) -> str:
        """Informa cómo se puede crear una instancia similar a la actual"""
        return f"Ident(length={self.__length}, alphabet='{self.__alphabet}')"

    def __str__(self) -> str:
        """Informa cómo está creada la instancia actual"""
        return f"Ident(length={self.__length}, alphabet='{self.__alphabet}')"
