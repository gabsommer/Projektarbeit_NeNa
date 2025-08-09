import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

filename = "ne_na_table.txt"
blocks = {}
lines_to_read = 0
current_block = None
data_x = []
data_y = []


with open(filename, "r") as ne_na_table_file:
    lines = ne_na_table_file.readlines()
    for line in lines:
        if line.startswith("FIT_"):
            if current_block is not None and data_x:
                blocks[current_block] = (data_x, data_y)
            current_block = line.strip()
            data_x = []
            data_y = []
        elif line.startswith("N ") and current_block is not None:
            lines_to_read = int(line.split()[1])
        elif lines_to_read > 0:
            parts = line.split()
            if len(parts)>=4:
                try:
                    data_x.append(float(parts[1]))
                    data_y.append(float(parts[2]))
                except ValueError:
                    pass
            lines_to_read -=1
if current_block is not None and data_x:
    blocks[current_block] = (data_x, data_y)


fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlabel("Interatomic Distance [Å]")
ax.set_ylabel("Energy [eV]")
ax.set_title("Pairpotential")
ax.grid(True)
ax.set_xlim(1,15)
ax.set_ylim(-1,1)
ax.plot(blocks["FIT_NENA"][0],blocks["FIT_NENA"][1], label = "Ne-Na")
ax.plot(blocks["FIT_NE2"][0],blocks["FIT_NE2"][1], label = "Ne-Ne")
ax.plot(blocks["FIT_NA2"][0],blocks["FIT_NA2"][1], label = "Na-Na")
plt.legend(loc = "upper right")

axins = inset_axes(ax, width="40%", height="40%", loc='lower right', bbox_to_anchor=(0.07, 0.06, 0.9, 0.9),  # y=1.05 moves it a bit up
                   bbox_transform=ax.transAxes)
axins.grid(True)
axins.plot(blocks["FIT_NENA"][0],blocks["FIT_NENA"][1], label = "Ne-Na")
axins.plot(blocks["FIT_NE2"][0],blocks["FIT_NE2"][1], label = "Ne-Ne")
axins.set_xlim(2.5,10)
axins.set_ylim(-0.003,0.005)
#mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.savefig("../Inhalt/Bilder/pairpotential.png")
plt.savefig("./pairpotential.png")

