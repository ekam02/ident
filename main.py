#!/usr/bin/python3
import argparse
from src.ident import Ident


parser = argparse.ArgumentParser(description='Ejemplo de CLI')
parser.add_argument('--amount', '-a', type=int, help='Cantidad de identificadores')
parser.add_argument('--length', '-l', type=int, help='Cantidad de caracteres')
parser.add_argument('--alphabet', type=str, help='Alfabeto usado')

args = parser.parse_args()

amount = args.amount if args.amount else 1
length = args.length if args.length else 8
alphabet = args.alphabet if args.alphabet else Ident.ALPHABET

for i in range(amount):
    print(Ident.id())
