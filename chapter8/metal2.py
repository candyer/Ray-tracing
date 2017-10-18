
from material import Material
from lambertian import random_in_unit_sphere

class Metal(Material):

	def __init__(self, albedo, f):
		self.albedo = albedo
		if f < 1:
			self.fuzz = f
		else:
			self.fuzz = 1


	def scatter(self, ray_in, rec, attenuation, scattered):
		reflected = self.reflect(ray_in.direction.unit_vector(), rec.normal)
		scattered.origin = rec.p
		scattered.direction = reflected + random_in_unit_sphere() * self.fuzz
		attenuation = self.albedo

		return (scattered.direction.dot(rec.normal) > 0, self.albedo, self.fuzz)