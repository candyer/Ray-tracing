
from material import Material

class Metal(Material):

	def __init__(self, albedo):
		self.albedo = albedo

	def scatter(self, ray_in, rec, attenuation, scattered):
		reflected = self.reflect(ray_in.direction.unit_vector(), rec.normal)
		scattered.origin = rec.p
		scattered.direction = reflected
		attenuation = self.albedo

		return (scattered.direction.dot(rec.normal) > 0, self.albedo)