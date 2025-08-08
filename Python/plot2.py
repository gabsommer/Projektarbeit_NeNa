from matplotlib import pyplot as plt
import numpy as np


ecoh = 0.02003

with open("S_dimer.txt", "r") as file:
    lines = file.readlines()
    data = [int(line.strip()) for line in lines]

unique_numbers = sorted(set(data))
frequencies = [data.count(num)/len(data) for num in unique_numbers]
x_values = range(unique_numbers[0]-3,unique_numbers[-1]+1)
y_values = [0,0,0] + frequencies


fig, ax1 = plt.subplots(figsize=(10,5))


ax1.set_xlabel('Number S of neon atoms removed')
ax1.set_ylabel('Relative Occurence')
ax1.set_title(f'Simulated Anealing of Sodium Dimer Defect')

ax1.bar(x_values,y_values,color='gray', edgecolor='black', width=0.6)

fig.tight_layout()
plt.savefig("../Inhalt/Bilder/optimaldimer.png")
print("Figure saved.")