import os
import argparse

# Tell argpase to handle arguments

parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")

# Tell argparse what arguments to expect
parser.add_argument("path", help="The filepath to the file to be analyzed.")

# Get arguments from the user
args = parser.parse_args()

filename = args.path
f = open(filename, 'r')

# Read the data in the file.
data = f.readlines()
f.close()

# Open a file for writing
base_filename = filename.split('.')
base_filename = base_filename[0]
output_filename = F'{base_filename}_Etot.txt'

f_write = open(output_filename, 'w+')

print(F'Writing output to {output_filename}')

f_write.write("Total Energy\n")

etot = []
# Loop through lines in the file.
for line in data:
    split_line = line.split()
    
    # Get information from the line
    if 'Etot' in line:
        # print(split_line[2])
        etot.append(split_line[2])
        
etot = etot[:-2]

for energy in etot:
    f_write.write(F"{energy}\n")
    


# Write information to new file.
f_write.close()