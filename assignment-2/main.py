import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(16, 9), dpi=200)

case_4_data = pd.read_csv('result-4.txt', header = None, names=['iteration','time'])
case_3_data = pd.read_csv('result-3.txt', header = None, names=['iteration','time'])
case_2_data = pd.read_csv('result-2.txt', header = None, names=['iteration','time'])
case_1_data = pd.read_csv('result-1.txt', header = None, names=['iteration','time'])

plt.plot(case_4_data['iteration'],case_4_data['time'], label="Physical Machine")
plt.plot(case_3_data['iteration'],case_3_data['time'], label="Virtual Machine")
plt.plot(case_2_data['iteration'],case_2_data['time'], label="Cloud Instance with Credits")
plt.plot(case_1_data['iteration'],case_2_data['time'], label="Cloud Instance No Credits")

plt.legend()
plt.show()