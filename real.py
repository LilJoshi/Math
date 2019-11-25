# Definition of Real Number class via Dedekind cut

class Real:
	""" For now can only be rational values. Also can only compare to rational
	values right now. """

	def __init__(self, f, rat_value):
		""" If it is rational; f must be consistent with rat_value """
		self.approx = rat_value
		self.epsilon = 0
		self.f = f
		self.floor = math.floor(self.approx)

	def greater_than(self, r):
		return f(r)

	def equals(self, r):
		""" eh """
		return self.approx == r

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

	@staticmethod
	def value(r):
		""" Main way to create real numbers from rational numbers. """
		return Real(r, lambda x: x < r)

zero = Real.value(0) # zero.f is equivalent to lambda x: x < 0

