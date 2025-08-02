

import matplotlib.pyplot as plt
import numpy as np
import pandas


data = pd.read_csv("Jobs.csv")
lang = data['LANGUAGE'].tolist()
java = data['JAVA'].tolist()
andr = data['ANDROID'].tolist()
py = data['PYTHON'].tolist()
c = data['C'].tolist()
Cp = data['C++'].tolist()


plt.bar(lang, java, width = 0.30, label = "Java")
plt.bar(lang, andr, width = 0.30, label = "ANDROID")
plt.bar(lang, py, width = 0.30, label = "PYTHON")
plt.bar(lang, c, width = 0.30, label = "C")
plt.bar(lang, cp, width = 0.30, label = "C++")
plt.xlabel("LANGUAGES")
plt.ylabel("JOBS")
plt.legend()
plt.grid()
plt.title("COMPARISON")
plt.show()