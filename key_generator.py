import argparse
import secrets
import string
from enum import Enum

class Case(Enum):
	LOWER = string.ascii_lowercase
	UPPER = string.ascii_uppercase
	BOTH = string.ascii_letters

def alfanumeric(length, case = Case.BOTH):
	alphabet = case.value + string.digits
	return ''.join(secrets.choice(alphabet) for i in range(length))

def hexadecimal(length):
	return secrets.token_hex(length//2)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A pre-shared key generator.')
	parser.add_argument('--length', default=18, type=int, help='The length of the secret to generate.')

	args = parser.parse_args()
	print(alfanumeric(args.length, Case.BOTH))
