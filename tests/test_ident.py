import re

from main import Ident

"""
La clase ``Ident()`` debe permitir crear instancias de objetos sin recibir argumentos de entrada. Por defecto,
son dos los argumentos esperados: El primero un número entero positivo (``length``); el segundo una cadena de
caracteres (``alphabet``).
"""


class TestIdent:
    def test_without_argument(self):
        """
        **SUMMARY**: Probar el comportamiento al crear una instancia sin argumentos.
        **EXPECTED RESULT**: El programa permite crear la instancia sin argumentos de entrada.
        **STEPS**:
        1. Crear una instancia del objeto sin argumentos.
        2. Comprobar que el valor asignado al parámetro ``length`` sea el valor ``8``; asimismo, comprobar que el valor
        asignado al parámetro ``alphabet`` sea el valor ``Ident.ALPHABET``.
        """
        without_arguments = Ident()
        assert without_arguments.length == 8
        assert without_arguments.alphabet == Ident.ALPHABET

    def test_method_id(self):
        """
        **SUMMARY**: Probar el comportamiento del método ``Ident.id()``.
        **EXPECTED RESULT**: El programa regresa una secuencia de caracteres de longitud ``8`` y abecedario
        ``Ident.ALPHABET``.
        1. llamado al método ``Ident.id()``.
        2. Comprobar que el valor impreso sea una secuencia de caracteres de longitud ``8`` y abecedario
        ``Ident.ALPHABET``.
        """
        assert re.search('[0-9a-z]', Ident.id())

    def test_with_argument(self):
        """
        **SUMMARY**: Probar el comportamiento al crear una instancia sin argumentos.
        **EXPECTED RESULT**: El programa permite crear la instancia sin argumentos de entrada.
        **STEPS**:
        1. Crear una instancia del objeto sin argumentos.
        2. Comprobar que el valor asignado al parámetro ``length`` sea el valor ``8``; asimismo, comprobar que el valor
        asignado al parámetro ``alphabet`` sea el valor ``Ident.ALPHABET``.
        """
        with_arguments = Ident(10, '0123456789abcdef')
        assert with_arguments.length == 10
        assert with_arguments.alphabet == '0123456789abcdef'


class TestIdentLength:
    def test_length_none(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar el valor None al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará el valor por defecto ``8``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar el valor None al parámetro ``length``, entregar _cadena de caracteres_ al parámetro ``alphabet``.
        """
        length_none = Ident(length=None, alphabet='texto')
        assert length_none.length == 8

    def test_length_zero(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar el valor 0 al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará el valor por defecto ``8``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar el valor 0 al parámetro ``length``, entregar cadena de caracteres al parámetro ``alphabet``.
        """
        length_zero = Ident(length=0, alphabet='testing')
        assert length_zero.length == 8

    def test_length_positive_int(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar un entero positivo al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará el valor entregado.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un entero positivo al parámetro ``length``, entregar cadena de caracteres al parámetro ``alphabet``.
        """
        length_positive = Ident(length=15, alphabet='dark')
        assert length_positive.length == 15
        length_positive.length = 33
        assert length_positive.length == 33

    def test_length_negative_int(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar un entero negativo al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará el valor por defecto ``8``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un entero negativo al parámetro ``length``, entregar cadena de caracteres al parámetro ``alphabet``.
        """
        length_negative = Ident(length=-5, alphabet='dark')
        assert length_negative.length == 8
        length_negative.length = -1505
        assert length_negative.length == 8

    def test_length_float(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar un número punto flotante al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará la parte entera positiva del número punto flotante
        entregado.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un número punto flotante al parámetro ``length``, entregar cadena de caracteres al parámetro
        ``alphabet``.
        """
        length_float = Ident(length=-5.9, alphabet='sixteen')
        assert length_float.length == 8
        length_float.length = 2.5
        assert length_float.length == 2
        length_float.length = 0.7
        assert length_float.length == 8

    def test_length_str_void(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar una cadena de caracteres vacía al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará la parte entera positiva del número punto flotante
        entregado.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar una cadena de caracteres vacía al parámetro ``length``, entregar cadena de caracteres al parámetro
        ``alphabet``.
        """
        length_str_void = Ident(length='', alphabet='thousand')
        assert length_str_void.length == 8
        length_str_void.length = ''
        assert length_str_void.length == 8

    def test_length_str_any(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar una cadena de caracteres al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará la parte entera positiva del número punto flotante
        entregado.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar una cadena de caracteres al parámetro ``length``, entregar cadena de caracteres al parámetro
        ``alphabet``.
        """
        length_str_void = Ident(length='this is a string', alphabet='thousand')
        assert length_str_void.length == 8
        length_str_void.length = 'this is an other string'
        assert length_str_void.length == 8


class TestIdentAlphabet:
    def test_alphabet_none(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar el valor None al parámetro ``alphabet``.
        **EXPECTED RESULT**: El atributo ``alphabet`` guardará el valor por defecto: ``Ident.ALPHABET``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un valor numérico válido al parámetro ``length``, entregar el valor None al parámetro
        ``alphabet``.
        """
        alphabet_none = Ident(length=50, alphabet=None)
        assert alphabet_none.alphabet == Ident.ALPHABET

    def test_alphabet_number(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar un valor numérico al parámetro ``alphabet``.
        **EXPECTED RESULT**: El atributo ``alphabet`` guardará el valor por defecto: ``Ident.ALPHABET``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un valor numérico válido al parámetro ``length``, entregar un valor numérico al parámetro
        ``alphabet``.
        """
        alphabet_number = Ident(length=56, alphabet=0)
        assert alphabet_number.alphabet == Ident.ALPHABET
        alphabet_number.alphabet = 88
        assert alphabet_number.alphabet == Ident.ALPHABET
        alphabet_number.alphabet = -7
        assert alphabet_number.alphabet == Ident.ALPHABET
        alphabet_number.alphabet = -3.8
        assert alphabet_number.alphabet == Ident.ALPHABET

    def test_alphabet_str_void(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar una cadena de caracteres vacía al parámetro ``alphabet``.
        **EXPECTED RESULT**: El atributo ``alphabet`` guardará el valor por defecto: ``Ident.ALPHABET``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un valor numérico válido al parámetro ``length``, entregar una cadena de caracteres vacía al
        parámetro ``alphabet``.
        """
        alphabet_str_void = Ident(length=7, alphabet='')
        assert alphabet_str_void.alphabet == Ident.ALPHABET
        alphabet_str_void.alphabet = ''
        assert alphabet_str_void.alphabet == Ident.ALPHABET

    def test_alphabet_str_any(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar una cadena de caracteres (no vacía) al parámetro ``alphabet``.
        **EXPECTED RESULT**: El atributo ``alphabet`` guardará los caracteres únicos de la cadena de caracteres.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar un valor numérico válido al parámetro ``length``, entregar una cadena de caracteres (no vacía) al
        parámetro ``alphabet``.
        """
        alphabet_str_any = Ident(length=6, alphabet='thousand')
        assert alphabet_str_any.alphabet == 'adhnostu'
        alphabet_str_any.alphabet = 'this is an other string'
        assert alphabet_str_any.alphabet == 'aeghinorst'


class TestIdentArgs:
    def test_args(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar valores válidos en el orden ``(length, alphabet)``.
        **EXPECTED RESULT**: Los valores se guardarán correctamente en los parámetros ``length`` y ``alphabet``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar valores válidos en el orden ``(length, alphabet)``.
        """
        test_args = Ident(7, '0123456789abcdef')
        assert test_args.length == 7
        assert test_args.alphabet == '0123456789abcdef'

    def test_args_first_arg(self) -> None:
        """
        **SUMMARY**: Probar comportamiento al entregar un valor numérico válido para la primera posición de la tuple
        (``length``).
        **EXPECTED RESULT**: El valor se guardará en el parámetro ``length``.
        **STEPS**:
        1. Crear instancia para la clase ``Ident()``.
        2. Entregar valor numérico válido para la primera posición de la tuple (``length``).
        """
        test_args_first_arg = Ident(7)
        assert test_args_first_arg.length == 7
        assert test_args_first_arg.alphabet == Ident.ALPHABET


class TestIdentKwargs:
    def test_length_with_none_argument(self):
        """
        **SUMMARY**: Probar el comportamiento al pasar el valor None al parámetro ``length``.
        **EXPECTED RESULT**: El atributo ``length`` guardará el valor por defecto ``8``.
        **STEPS**:
        1. Crear una instancia del objeto, entregando el valor None el parámetro ``length``.
        2. Comprobar que el valor asignado al atributo ``length`` sea el valor ``8``.
        """
        a = Ident(length=None)
        assert a.length == 8

    def test_instance_with_one_argument(self):
        """
        **SUMMARY**: Probar instancia con un unico argumento de entrada.
        **EXPECTED RESULT**: El tamaño debería quedar con el valor por defecto.
        **STEPS**:
        1. Crear una instancia del objeto entregando el valor None el parámetro ``length``.
        2. Comprobar que el valor asignado al atributo ``length`` sea el valor ``8``.
        """
        only_length_with_argument = Ident(length=None)
        assert only_length_with_argument.length == 8
        only_alphabet_with_argument = Ident(alphabet='Abecedario')
        assert only_alphabet_with_argument.alphabet == 'Aabcdeior'
