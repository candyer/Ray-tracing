
from vec3 import Vec3
from ray import Ray
from math import sqrt

def hit_sphere(center, radius, ray):
	oc = ray.origin - center
	a = ray.direction.dot(ray.direction)
	b = 2.0 * oc.dot(ray.direction)
	c = oc.dot(oc) - radius * radius
	discriminant = b * b - 4 * a * c
	if discriminant < 0:
		return -1.0
	else:
		return (-b - sqrt(discriminant)) / ( 2.0 * a)

def color(ray):
	t = hit_sphere(Vec3(0, 0, -1), 0.5, ray)
	if t > 0.0:
		N = (ray.point_at_parameter(t) - Vec3(0, 0, -1)).unit_vector()
		return Vec3(N.x() + 1, N.y() + 1, N.z() + 1) * 0.5
	unit_direction = ray.direction.unit_vector()
	t = 0.5 * (unit_direction.y() + 1.0)
	return Vec3(1.0, 1.0, 1.0) * (1.0 - t) + Vec3(0.5, 0.7, 1.0) * t

def main():
	with open("output1.ppm", "w") as f:
		nx, ny = 200, 100
		header = "P3\n{} {}\n255\n".format(nx, ny)
		f.write(header)
		lower_left_corner = Vec3(-2.0, -1.0, -1.0)
		horizontal = Vec3(4.0, 0.0, 0.0)
		vertical = Vec3(0.0, 2.0, 0.0)
		origin = Vec3(0.0, 0.0, 0.0)
		for j in range(ny-1, -1, -1):
			for i in range(0, nx):
				u = float(i) / float(nx)
				v = float(j) / float(ny)
				direction = lower_left_corner + horizontal * u + vertical * v
				ray = Ray(origin, direction)
				col = color(ray)
				ir = int(255.99 * col.r())
				ig = int(255.99 * col.g())
				ib = int(255.99 * col.b())
				line = "{} {} {}\n".format(ir, ig, ib)
				f.write(line)
main()
 







