from matplotlib import pyplot as plt
import _pickle as pickle







with open("S_mono.txt", "r") as file:
    lines=file.readlines()
    data = [int(line.strip()) for line in lines]




unique_numbers = sorted(set(data))  # Find unique numbers
frequencies = [data.count(num)/len(data) for num in unique_numbers]  # Count each number
# Plot
plt.bar(unique_numbers, frequencies,color='gray', edgecolor='black', width=0.6)
plt.xlabel('Number of neon atoms removed')
plt.ylabel('Relative Occurence')
plt.title(f'Simulated Anealing ({len(data)} sweeps) of Sodium Monomer')
plt.show()