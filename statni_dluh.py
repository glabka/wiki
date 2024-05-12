import matplotlib as mtl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from numpy import array
import numpy as np
import locale

# data copied from https://www.mfcr.cz/cs/rozpoctova-politika/rizeni-statniho-dluhu/statistiky/struktura-a-vyvoj-statniho-dluhu
data = [158.8, 157.3, 154.4, 155.2, 173.1, 194.7, 228.4, 289.3, 345.0, 395.9, 493.2, 592.9, 691.2, 802.5, 892.3, 999.8, 1178.2, 1344.1, 1499.4, 1667.6, 1683.3, 1663.7, 1673.0, 1613.4, 1624.7, 1622.0, 1640.2, 2049.7, 2465.7, 2894.8, 3110.9]

data_diff = list([number - previous for number, previous in zip(data[1:], data[0:-1])])
years = list(range(1994,2024))
years = [str(year) for year in years]
data_diff_years = np.array

fig, ax = plt.subplots()


for data_point, year in zip(data_diff, years):
    if data_point > 0:
        color = 'red'
    else:
        color = 'green'
    p = ax.bar(year, data_point, width=0.8, color=color)  
    str_number = '{:,.1f}'.format(data_point).replace('.', ',') # decimal point to decimal column
    ax.bar_label(p, label_type='edge', fontsize='x-small', fmt=str_number)


ax.set_title('Růst (nebo pokles) státního dluhu v letech 1994 až 2023')
ax.set_xlabel('roky')
ax.set_ylabel('miliard Kč')

legend_elements = [Patch(facecolor='red', edgecolor='red', label='růst dluhu'), Patch(facecolor='green', edgecolor='green', label='pokles dluhu')]
ax.legend(handles=legend_elements)
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='center', fontsize='x-small')
fig.set_size_inches(13,4.5)

plt.savefig('statni_dluh_cr.svg')

plt.show()