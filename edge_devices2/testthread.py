import os
import multiprocessing

# Get the number of CPU cores
num_cores = multiprocessing.cpu_count()

# Print the result
print(f"Number of CPU cores: {num_cores}")
