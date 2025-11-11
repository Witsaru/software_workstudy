import csv
import time
import random
import numpy as np
import os  # Import os module to handle directory operations

# Create data
list_n = [i for i in range(1, 101)]
s1 = [random.uniform(1, 5) for j in range(100)]
s2 = [random.uniform(1, 5) for j in range(100)]
s3 = [random.uniform(1, 5) for j in range(100)]
s4 = [random.uniform(10, 15) for j in range(100)]
list_t = [random.uniform(14, 60) for j in range(100)]

# Combine both lists into a 2D array
np_num = np.array([list_n, s1, s2, s3, s4, list_t])

# Define the filename and path
directory = 'TESTlab/csvTest/'
filename = f'{directory}tocips_file_{time.strftime("%Y%m%d_%H%M%S", time.gmtime())}.csv'

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Create the CSV file
with open(filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write header
    header = ['item']
    for i in range(4):
        header.append(f'Subtime{i+1}')  # Use i+1 to start counting from 1

    header.append('totaltime')  # Append total time at the end
    
    # Write the header to the CSV
    writer.writerow(header)

    # Write the data using zip to combine both lists
    for values in np_num.T:  # Transpose to iterate over rows
        writer.writerow(values)  # Write each row of data

print(f"Data written to {filename}")
