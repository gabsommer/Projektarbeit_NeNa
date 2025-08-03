from matplotlib import pyplot as plt
import _pickle as pickle
import numpy as np




ecoh = 0.02003


with open("S_mono.txt", "r") as file:
    lines=file.readlines()
    data = [int(line.strip()) for line in lines]


with open("./pickles/bf_results_1.0e-7_2l", "rb") as file:
    datapick = pickle.load(file)
bruteforceplot = np.array([])

for i in range(11):
    S = i
    energy = datapick[S-2]['neon_energies'].sum()+datapick[S-2]['sodium_energies'].sum()-2*ecoh*S
    bruteforceplot = np.append(bruteforceplot,energy)

print(bruteforceplot)

unique_numbers = sorted(set(data))  # Find unique numbers
frequencies = [data.count(num)/len(data) for num in unique_numbers]  # Count each number
# Plot
plt.bar(unique_numbers, frequencies,color='gray', edgecolor='black', width=0.6)
plt.xlabel('Number of neon atoms removed')
plt.ylabel('Relative Occurence')
plt.title(f'Simulated Anealing ({len(data)} sweeps) of Sodium Monomer')
#plt.show()