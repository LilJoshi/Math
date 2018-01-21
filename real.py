# Definition of Real Number class via Dedekind cut

class Real:

	def __init__(self, f, rat_val=None):
		self.f = f
		self.val = rat_val

	def greater_than(self, r):
		return f(r)

	def equals(self, r):
		return self.val == r

	def greater_than_or_equals(self, r):
		return greater_than(r) or equals(r)

	def less_than(self, r):
		return not greater_than_or_equals(r)

	def less_than_or_equals(self, r):
		return not greater_than(r)

	@staticmethod
	def sqrt(r):
		return Real(lambda x: x*x < r)

	@staticmethod
	def root(r, n):
		return Real(lambda x: x**n < r)

	@staticmethod
	def log(r, b):
		return Real(lambda x: b**x < r)


is_negative = lambda r: r < 0

