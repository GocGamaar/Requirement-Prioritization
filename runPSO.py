from PSO import PSO

def fitting_fn(genome):
	x1, x2, x3, x4, x5, x6 = genome

	if x5==x6:
		x6=0
	if x4==x5 or x4==x6:
		x5 = x6 = 0
	if x4>x5 and x4>x6:
		x5 = x6 = 0
	if x5>x6 and x5>x4:
		x4 = x6 = 0
	if x6>x4 and x6>x5:
		x4 = x5 = 0

	if x3==0:
		return 0
	else:
		return x1 + (10-(x2/x3)) + (x4*9) + (x5*5) + (x6*1)

instance = PSO(
	func=fitness_fn, dim=3,
	lb=[1, 1, 0, 0, 0],
	ub=[20, 20, 2, 2, 2]
	)
result = instance.run(max_iter=100)

print("Best values of x: ", result.gbest_x)
print("Best values of f(x): ",result.gbest_y)