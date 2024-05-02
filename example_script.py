import pandas as pd

# Membuat data dummy
data = {
    'Nama': ['Ali', 'Budi', 'Citra', 'Dewi'],
    'Umur': [22, 25, 24, 23],
    'Kota': ['Jakarta', 'Surabaya', 'Bandung', 'Yogyakarta']
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

