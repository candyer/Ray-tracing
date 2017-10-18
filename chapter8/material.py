
from abc import ABCMeta, abstractmethod

class Material:
	__metaclass__ = ABCMeta

	@abstractmethod
	def scatter(self, ray_in, rec, attenuation, scattered):
		pass

	def reflect(self, v, n):
		return v - n * (v.dot(n) * 2)



