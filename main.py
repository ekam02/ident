import random


class Ident:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789'

    @staticmethod
    def id():
        return ''.join(random.choices(Ident.ALPHABET, k=8))

    @staticmethod
    def set(*args) -> any:
        def core(*_args):
            unique_characters = []
            for character in _args:
                if character not in unique_characters:
                    unique_characters.append(character)
            return unique_characters

        if len(args) == 1:
            return ''.join(core(*args[0]))
        elif len(args) > 1:
            return core(*args)
        else:
            return ''

    @classmethod
    def is_positive_number(cls, number: int) -> bool:
        result = False
        try:
            result = True if number >= 1 else False
        except TypeError:
            print(f"El argumento {number} debería ser tipo numérico")
        finally:
            return result

    @classmethod
    def is_alphabet(cls, alphabet: str) -> bool:
        result = False
        try:
            result = True if len(alphabet) > 1 and isinstance(alphabet, str) else False
        except TypeError:
            print(f"El argumento {alphabet} debería ser tipo cadena de caracteres")
        finally:
            return result

    @classmethod
    def normalize_length(cls, length: int) -> int:
        return int(length) if cls.is_positive_number(length) else 8

    @classmethod
    def normalize_alphabet(cls, alphabet: str) -> str:
        return cls.set(alphabet) if cls.is_alphabet(alphabet) else cls.ALPHABET

    def __init__(self, *args, **kwargs) -> None:
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
        return self.__length

    @length.setter
    def length(self, length: int) -> None:
        self.__length = self.normalize_length(length)

    @property
    def alphabet(self) -> str:
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, alphabet: str) -> None:
        self.__alphabet = self.normalize_alphabet(alphabet)

    def identifier(self, amount: int = 1) -> list:
        amount = amount if self.is_positive_number(amount) else 1
        return [''.join(random.choices(self.__alphabet, k=self.__length)) for _ in range(amount)]

    def __str__(self) -> str:
        return f"Ident(length={self.__length}, alphabet='{self.__alphabet}')"
