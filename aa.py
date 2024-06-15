import pandas as pd

# Örnek veri çerçevesi oluşturma
data = {
    'Name': ['Ali', 'Ayşe', 'Mehmet', 'Fatma'],
    'Age': [25, 30, 22, 35],
    'City': ['Istanbul', 'Ankara', 'Izmir', 'Antalya']
}

df = pd.DataFrame(data)

# Veri çerçevesini ekrana yazdırma
print("Original DataFrame:")
print(df)

# Yaşa göre filtreleme (30 yaşından büyük olanlar)
filtered_df = df[df['Age'] > 30]

# Filtrelenmiş veri çerçevesini ekrana yazdırma
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Yeni bir sütun ekleme
df['Is_Adult'] = df['Age'] >= 18

# Yeni sütun ile güncellenmiş veri çerçevesini ekrana yazdırma
print("\nUpdated DataFrame with 'Is_Adult' column:")
print(df)
