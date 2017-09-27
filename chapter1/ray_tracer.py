def generate_gradient():
	nx, ny = 200, 100
	print 'P3\n{} {}\n255'.format(nx, ny)
	for j in range(ny - 1, -1, -1):
		for i in range(nx):
			r = i / float(nx)
			g = j / float(ny)
			b = 0.2
			ir = int(255.99 * r)
			ig = int(255.99 * g)
			ib = int(255.99 * b)
			print '{} {} {}'.format(ir, ig, ib)
	
generate_gradient()

# run it on the terminal
# $ python ray_tracer.py > output.ppm