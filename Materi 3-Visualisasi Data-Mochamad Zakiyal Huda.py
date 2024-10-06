import numpy as np
import matplotlib.pyplot as plt

g = 9.8  
v0 = 0  
h0 = 100  


t = np.sqrt(2 * h0 / g)
print("Waktu Yang Diperlukan Benda Untuk Mencapai Tanah =", t, "s")

T = np.linspace(0, t, 100)
h = h0 - 0.5 * g * T**2
print("Posisi (ketinggian) sebagai fungsi waktu =", h, "m")
v = g * T
print("Kecepatan sebagai fungsi waktu =", v, "m/s")
print("\n")


fig, ax1 = plt.subplots()
ax1.plot(T, h, label='Height (m)', color='b')
ax1.set(xlabel='t (s)', ylabel='h (m)', title='Posisi terhadap Waktu')
ax1.axhline(0, color='black',linewidth=0.5, ls='--')
ax1.grid()
ax1.legend()


fig, ax2 = plt.subplots()
ax2.plot(T, v, label='Velocity (m/s)', color='r')
ax2.set(xlabel='t (s)', ylabel='v (m/s)', title='Kecepatan terhadap Waktu')
ax2.axhline(0, color='black',linewidth=0.5, ls='--')
ax2.grid()
ax2.legend()

plt.show()
