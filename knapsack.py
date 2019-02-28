from random import randint
from fractions import gcd

def decrypt(message, privkey):
	return False

def encrypt(message, pubkey):
	sum = 0
	for i in range(len(message)):
		sum += message[i] * pubkey[i]
	return sum

def binarize(message):
	return [int(i) for i in "{:08b}".format(message)]

def generate_keys(n):
	w = [random.randint(1, 10)]
	multiplier = randint(2, 4)
	for i in range(n):
		w += [randint(sum(w), multiplier*sum(w))]

	q = randint(sum(w), multiplier*sum(w))
	r = randint(1, q)

	while gcd(q, r) != 1:
		r = randint(0, q)

	B = [(w[i] * r) % q for i in range(len(w))]
	
	return B, w, q, r

if __name__ == "__main__":
	q = 881
	r = 588
	w = [2, 7, 11, 21, 42, 89, 180, 354]
	B = [295, 592, 301, 14, 28, 353, 120, 236]
	message = binarize(97)
	print(encrypt(message, B))
