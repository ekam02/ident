#!/usr/bin/python3
import argparse
from src.ident import Ident


parser = argparse.ArgumentParser(description='Ident CLI')
parser.add_argument('--amount', '-a', type=int, help='Define la cantidad de identificadores a imprimir.')
parser.add_argument('--length', '-l', type=int, help='Define la cantidad de caracteres en la secuencia.')
parser.add_argument('--alphabet', type=str, help='Define el alfabeto a usar.')

args = parser.parse_args()

amount = args.amount if args.amount else 1
length = args.length if args.length else 8
alphabet = args.alphabet if args.alphabet else Ident.ALPHABET

identify = Ident(length=length, alphabet=alphabet)

for i in range(amount):
    print(identify.identifier()[0])
