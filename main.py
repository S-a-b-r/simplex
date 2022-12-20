from simplex import Simplex
objective = ('maximize', '3x_1 + 8x_2')
constraints = ['1x_1 + 7x_2 <= 32', '2x_1 + 5x_2 <= 42', '3x_1 + 4x_2 <= 62', '2x_1 + 1x_2 = 34']
Lp_system = Simplex(num_vars=2, constraints=constraints, objective_function=objective)
print(Lp_system.solution)
print(Lp_system.optimize_val)