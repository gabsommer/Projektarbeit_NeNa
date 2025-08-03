from matplotlib import pyplot as plt
import _pickle as pickle
import numpy as np




ecoh = 0.02003


with open("S_mono.txt", "r") as file:
    lines=file.readlines()
    data = [int(line.strip()) for line in lines]


with open("./pickles/bf_results_1.0e-7_4l", "rb") as file:
    datapick = pickle.load(file)
bruteforcedata = np.array([])

for i in range(len(datapick)):
    S = i
    energy = datapick[i]['neon_energies'].sum() + datapick[i]['sodium_energies'].sum() - S*ecoh
    bruteforcedata = np.append(bruteforcedata,energy)
bruteforcedata = bruteforcedata[3:]



unique_numbers = sorted(set(data))  # Find unique numbers
frequencies = [data.count(num)/len(data) for num in unique_numbers]  # Count each number
# Plot


fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.bar(unique_numbers,frequencies,color='gray', edgecolor='black', width=0.6)

ax1.set_xlabel('Number of neon atoms removed')
ax1.set_ylabel('Relative Occurence')
ax1.set_title(f'Simulated Anealing ({len(data)} sweeps) of Sodium Monomer')

ax2 = ax1.twinx()
ax2.set_ylabel('Minimum Energies [eV]', color = "black", labelpad=10)
ax2.plot(range(5,len(bruteforcedata)+5), bruteforcedata, color = "black", marker="x" )

fig.tight_layout()
plt.savefig("../Inhalt/Bilder/optimal_defect_simulated_annealing.png")