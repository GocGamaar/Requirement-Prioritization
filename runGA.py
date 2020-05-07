from GA import GeneticAlgorithm

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

population_size = 100; genome_length = 5

ga = GeneticAlgorithm(
	fitness_function, 
	pop_size=population_size, 
	genome_length=genome_length,
	lb=[1, 1, 0, 0, 0],
	ub=[20, 20, 2, 2, 2]
	)
ga.generate_binary_population()

# No. of pairs of individuals to be picked to mate
ga.number_of_pairs = 4

# Selective pressure from interval [1.0, 2.0]
# the lower value, the less will the fitness play role

ga.selective_pressure = 1.4
ga.mutation_rate = 0.1

ga.run(100)

best_genome, best_fitness = ga.get_best_genome()
print("Best values for x: ", (1*best_genome))
print("Best value for f(x):", best_fitness)

# population = ga.population
# print(population, " population")

# fitness_vector = ga.get_fitness_vector()
# print(fitness_vector, " fit vec")