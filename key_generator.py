import argparse
import secrets
import string

def alfanumeric(length):
	alphabet = string.ascii_letters + string.digits
	return ''.join(secrets.choice(alphabet) for i in range(length))

def hexadecimal(length):
	return secrets.token_hex(length//2)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A pre-shared key generator.')
	parser.add_argument('--length', default=18, type=int, help='The length of the secret to generate.')
	args = parser.parse_args()

	print(alfanumeric(args.length))