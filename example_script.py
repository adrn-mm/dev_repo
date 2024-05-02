import pandas as pd

# Membuat data dummy
data = {
    'Nama': ['Adrian', 'Erickson'],
    'Umur': [25, 25],
    'Kota': ['Depok', 'Depok']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
print("DataFrame:")
print(df)

# Mengonversi DataFrame ke CSV
csv_data = df.to_csv(index=False)
print("\nData CSV:")
print(csv_data)
