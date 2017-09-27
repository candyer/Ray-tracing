
from ray_tracer import Vec3
import unittest
from random import randint as r
class TestStringMethods(unittest.TestCase):

	def test_neg(self):
		vec = Vec3(-1, 0, 2)
		result = -vec
		# self.assertEqual(result.x(), 1)
		# self.assertEqual(result.y(), 0)
		# self.assertEqual(result.z(), -2)
		self.assertEqual(result, Vec3(1, 0, -2))

	def test_neg_fancy(self):
		for _ in range(100):
			vec = Vec3(r(-10, 10), r(-10, 10), r(-10, 10))
			result = -(-vec)
			self.assertEqual(result, vec)

	def test_pos(self):
		for _ in range(100):
			vec = Vec3(r(-10, 10), r(-10, 10), r(-10, 10))
			result = +vec
			self.assertEqual(result, vec)

	def test_add(self):
		vec1 = Vec3(-1, 0, 1)
		vec2 = Vec3(1, 2, 3)
		res = vec1 + vec2
		self.assertEqual(res, Vec3(0, 2, 4))

	def test_sub(self):
		vec1 = Vec3(-1, 0, 1)
		vec2 = Vec3(1, 2, 0)
		res = vec1 - vec2
		self.assertEqual(res, Vec3(-2, -2, 1))

	def test_mul(self):
		vec1 = Vec3(-1, 0, 1)
		vec2 = Vec3(1, 2, 3)
		res = vec1 * vec2
		self.assertEqual(res, Vec3(-1, 0, 3))

	def test_div(self):
		vec1 = Vec3(-1, 0, 1)
		vec2 = Vec3(1, 2, 3)
		res = vec1 / vec2
		self.assertEqual(res, Vec3(-1, 0, 1/3.0))

	def test_squared_length(self):
		for _ in range(100):
			a, b, c = r(-10, 10), r(-10, 10), r(-10, 10)
			tmp = a * a + b * b + c * c
			vec = Vec3(a, b, c)
			res = vec.squared_length()
			self.assertEqual(res, tmp)		

	def test_dot(self):
		for _ in range(100):
			a1, b1, c1 = r(-10, 10), r(-10, 10), r(-10, 10)
			a2, b2, c2 = r(-10, 10), r(-10, 10), r(-10, 10)
			vec1 = Vec3(a1, b1, c1)
			vec2 = Vec3(a2, b2, c2)
			res = a1 * a2 + b1 * b2 + c1 * c2
			self.assertEqual(res, vec1.dot(vec2))

	def test_cross(self):
		for _ in range(100):
			a1, b1, c1 = r(-10, 10), r(-10, 10), r(-10, 10)
			a2, b2, c2 = r(-10, 10), r(-10, 10), r(-10, 10)
			vec1 = Vec3(a1, b1, c1)
			vec2 = Vec3(a2, b2, c2)
			res = Vec3(b1 * c2 - c1 * b2, -(a1 * c2 - c1 * a2), a1 * b2 - b1 * a2)
			self.assertEqual(res, vec1.cross(vec2))					

	def test_unit_vector(self):
		for _ in range(100):
			a, b, c = r(-10, 10), r(-10, 10), r(-10, 10)
			vec = Vec3(a, b, c)
			square_root = vec.length
			res = Vec3(a / square_root, b / square_root, c / square_root)
			self.assertEqual(res, vec.unit_vector())		

if __name__ == '__main__':
    unittest.main()