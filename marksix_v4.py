import numpy as np
from sklearn.preprocessing import normalize

#change number of iterations
num_iterations = 2

#balls range from 1 to 49
all_balls = np.arange(1, 50, dtype=int)

#generate rng object
rng = np.random.default_rng()

#generate probability for each entry
prob = rng.standard_normal(49)

#normalize then make the sum of all prob to 1
norm_prob = prob/ sum(prob)
print(norm_prob)

#generate marksix result
for _ in range(num_iterations):
    result = np.sort(rng.choice(all_balls, 6, replace=False, p=norm_prob, shuffle=True))
    print(result)
