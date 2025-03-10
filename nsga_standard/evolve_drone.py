import os
from simevo.population import generate_population_lhs
from simevo.algorithms.nsga import nsga

pop_num = 100
num_gen = 200

root_path = "./nsga_standard/Logs_1/"

for i in range(1,2):
    print(f"Run number {i}...")
    save_path = os.path.join(root_path, f"run{i}")
    if not os.path.exists(save_path):
            os.mkdir(save_path)

    # Generate initial population
    population = generate_population_lhs(pop_num, num_attributes=5)
    

    # Evolve drone
    nsga(population, num_gen, eval_verbose=0, file_path=save_path)

