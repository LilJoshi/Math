# Orderings of countable sets
# Beyond just integer sequences

from numbertheory import gcd
from numbertheory import Rational

def integers():
	yield 0
	for i in naturals():
		yield i
		yield -i

def rationals():
	""" via Cantor diagonalization """
	n = 2
	while True:
		p = 1
		while p < n:
			if gcd(p, n-p) == 1:
				yield Rational(p, n-p)
			p += 1
		n += 1

def rationals_calkin_wilf():
	""" via Calkin-Wilf sequence, 
	https://www.math.upenn.edu/~wilf/website/recounting.pdf """

def rationals_calkin_wilf_closed_form(p = 1, q = 1):
	""" this formula is from Proofs by the BOOK, credited to Moshe Newman """
	yield Rational(p, q)
	yield from rationals_calkin_wilf_closed_form(q, 2*q*(p//q)-p+q)
