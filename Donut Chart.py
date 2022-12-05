import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['A','B','C','D'])
sizes = np.array([35,25,25,15])
colors = np.array(['MediumVioletRed',
                    'Violet',
                    'DodgerBlue',
                    'DeepSkyBlue'])

plt.pie(sizes, labels = labels,
                colors = colors,
                wedgeprops = {'width':0.4},
                autopct = '%1.1f%%',
                pctdistance = 0.8)

plt.title("Donut Chart")

plt.legend(title = "segments:",
            loc = 'upper left')

plt.show()