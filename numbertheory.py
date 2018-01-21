# Number theory

import math

def is_square(n):
	return math.sqrt(n) % 1 <= 0


def gcd(p, q):
	""" Euclid's algorithm for finding gcd """
	if p == q:
		return p
	elif p < q:
		return gcd(q, p)
	else:
		return gcd(p-q, q)

def is_prime(p):
	if p <= 1:
		return False
	for i in range(2, math.floor(math.sqrt(p))+1):
		if gcd(p, i) > 1:
			return False
	return True

class Rational:
	def __init__(self, p, q):
		g = gcd(p, q)
		self.p = p // g
		self.q = q // g

	def __str__(self):
		return str(self.p)+"/"+str(self.q)

	def __repr__(self):
		return str(self)