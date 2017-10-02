
class Ray:
	def __init__(self, origin, direction):
		self.origin = origin
		self.direction = direction

	def point_at_parameter(self, t):
		return self.origin + self.direction * t

import unittest
class TestStringMethods(unittest.TestCase):
	def test_point_at_parameter(self):
		from random import randint as r
		for _ in range(100):
			origin = r(-10, 10)
			direction = r(-10, 10)
			t = r(-10, 10)
		ray = Ray(origin, direction)
		res = origin + direction * t
		self.assertEqual(res, ray.point_at_parameter(t))

if __name__ == '__main__':
    unittest.main()