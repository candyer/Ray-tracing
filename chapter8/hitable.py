
from abc import ABCMeta, abstractmethod


class Hitable:
	__metaclass__ = ABCMeta

	@abstractmethod
	def hit(self, ray, tmin, tmax, rec):
		pass