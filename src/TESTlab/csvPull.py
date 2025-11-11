import csv
import time
import random
import numpy as np

list_n = [i for i in range(1, 101)]
list_t = [random.uniform(14, 60) for j in range(100)]

# Combine both lists into a 2D array
np_num = np.array([list_n, list_t])

# Create the CSV file
filename = f'TESTlab/csvTest/employee_file_{time.strftime("%Y%m%d_%H%M%S", time.gmtime())}.csv'
with open(filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write header
    writer.writerow(['item', 'time'])
    
    # Write the data using zip to combine both lists
    for n, t in zip(list_n, list_t):
        writer.writerow([n, t])

print(f"Data written to {filename}")
