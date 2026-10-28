from __future__ import annotations

import random
import re
import string
from typing import Union, cast

NumberLike = Union[int, float, str]


class Ident:
    ALPHABET = string.digits + string.ascii_lowercase

    @staticmethod
    def id() -> str:
        """Entrega un Ident alfanumérico de 8 caracteres de longitud"""
        return "".join(random.choices(Ident.ALPHABET, k=8))

    @classmethod
    def is_positive_number(cls, number: object) -> bool:
        """Comprueba si ``number`` es un entero positivo"""
        try:
            return cast(Union[int, float], number) >= 1
        except TypeError:
            print(f"El argumento {number} debería ser tipo 'Numérico'.")
            return False

    @classmethod
    def is_alphabet(cls, alphabet: object) -> bool:
        """Comprueba si ``alphabet`` es de tipo str"""
        try:
            return len(cast(str, alphabet)) > 1 and isinstance(alphabet, str)
        except TypeError:
            print(f"El argumento {alphabet} debería ser tipo 'Cadena de Caracteres'.")
            return False

    @classmethod
    def normalize_length(cls, length: object) -> int:
        """Determina si ``length`` es adecuado o no para Ident"""
        return int(cast(NumberLike, length)) if cls.is_positive_number(length) else 8

    @classmethod
    def normalize_alphabet(cls, alphabet: object) -> str:
        """Determina si ``alphabet`` es adecuado o no para Ident"""

        def sort(sentence: list[str]) -> list[str]:
            """Organiza el contenido de ``sentence``"""
            sentence.sort()
            return sentence

        if not cls.is_alphabet(alphabet):
            return cls.ALPHABET

        characters = [
            character
            for character in set(cast(str, alphabet))
            if not re.search(r"\s", character)
        ]
        return "".join(sort(characters))

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Instancia un objeto Ident"""
        if args:
            self.__length = self.normalize_length(args[0]) if len(args) > 0 else 8
            self.__alphabet = (
                self.normalize_alphabet(args[1]) if len(args) > 1 else self.ALPHABET
            )
        elif kwargs:
            self.__length = (
                self.normalize_length(kwargs["length"]) if "length" in kwargs else 8
            )
            self.__alphabet = (
                self.normalize_alphabet(kwargs["alphabet"])
                if "alphabet" in kwargs
                else self.ALPHABET
            )
        else:
            self.__length = 8
            self.__alphabet = self.ALPHABET

    @property
    def length(self) -> int:
        """Informa la longitud de la instancia"""
        return self.__length

    @length.setter
    def length(self, length: object) -> None:
        """Asigna una longitud para la instancia"""
        self.__length = self.normalize_length(length)

    @property
    def alphabet(self) -> str:
        """Informa el abecedario de la instancia"""
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet: object) -> None:
        """Asigna el abecedario para la instancia"""
        self.__alphabet = self.normalize_alphabet(alphabet)

    def identifier(self, amount: object = 1) -> list[str]:
        """Entrega un listado de secuencias representativas a Ident"""
        resolved_amount = cast(int, amount) if self.is_positive_number(amount) else 1
        return [
            "".join(random.choices(self.__alphabet, k=self.__length))
            for _ in range(resolved_amount)
        ]

    def __repr__(self) -> str:
        """Informa cómo se puede crear una instancia similar a la actual"""
        return f"Ident(length={self.__length}, alphabet='{self.__alphabet}')"

    def __str__(self) -> str:
        """Informa cómo está creada la instancia actual"""
        return f"Ident(length={self.__length}, alphabet='{self.__alphabet}')"
