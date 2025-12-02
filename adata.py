# Import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset
data = pd.read_csv('nilai_siswa.csv', sep=';')

# Tampilkan informasi dataset
print("Informasi Dataset:")
data.info()

# Tampilkan 5 data pertama
print("\n5 Data Pertama:")
print(data.head())

# Tampilkan statistik deskriptif
print("\nStatistik Deskriptif:")
print(data.describe())

# Hitung rata-rata, median, dan modus
print("\nRata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# Tampilkan nilai per mata pelajaran
print("\n--- Matematika ---")
matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

print("\n--- Bahasa Inggris ---")
bahasa_inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(bahasa_inggris)

print("\n--- Bahasa Indonesia ---")
bahasa_indonesia = data[data['Matpel'] == 'Bahasa Indonesia']
print(bahasa_indonesia)

print("\n--- Produktif ---")
produktif = data[data['Matpel'] == 'Produktif']
print(produktif)

print("\n--- Fisika ---")
fisika = data[data['Matpel'] == 'Fisika']
print(fisika)

# Tampilkan nilai maksimum dan minimum per mapel
print("\nNilai Maksimum dan Minimum per Mapel:")
print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

# Buat grafik batang rata-rata nilai per mapel
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# Buat diagram boxplot
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()