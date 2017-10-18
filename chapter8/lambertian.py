
from material import Material
from vec3 import Vec3
from random import random

def random_in_unit_sphere():
	p = Vec3(random(), random(), random()) * 2 - Vec3(1.0, 1.0, 1.0)
	while p.dot(p) >= 1.0:
		p = Vec3(random(), random(), random()) * 2 - Vec3(1.0, 1.0, 1.0)
	return p

class Lambertian(Material):
	def __init__(self, albedo):
		self.albedo = albedo

	def scatter(self, ray_in, rec, attenuation, scattered):
		target = rec.p + rec.normal + random_in_unit_sphere()
		scattered.origin = rec.p
		scattered.direction = target - rec.p
		attenuation = Vec3(1.0, 1.0, 1.0)
		return (True, self.albedo)
