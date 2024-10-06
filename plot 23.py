import pandas as pd
import matplotlib.pyplot as plt
# Membaca file Excel
file_path = r"D:\File Zaki\semester 5\prakfiskom\Materi 3\plot 23.xlsx"
data = pd.read_excel(file_path)
# Asumsi bahwa kolom pertama adalah X dan kolom kedua adalah Y
X = data.iloc[:, 0] # Kolom pertama (nilai sumbu x)
Y = data.iloc[:, 1] # Kolom kedua (nilai sumbu y)
# Plotting data
plt.plot(X, Y)
plt.title('Data dari "data1.xlsx"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
