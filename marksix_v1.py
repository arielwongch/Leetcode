import numpy as np

#change number of iterations
num_iterations = 2

#balls range from 1 to 49
all_balls = np.arange(1, 50, dtype=int)

#generate rng object
rng = np.random.default_rng()

#generate marksix result
for _ in range(num_iterations):
    result = np.sort(rng.choice(all_balls, 6, replace=False, shuffle=True))
    print(result)