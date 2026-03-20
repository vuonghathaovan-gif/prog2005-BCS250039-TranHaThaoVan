import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('california_cities.csv')
top10 = df.sort_values('area_total_km2', ascending=False).head(10)
top10 = top10.sort_values('area_total_km2', ascending=True)
plt.barh(top10['city'], top10['area_total_km2'])
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')
plt.tight_layout()
plt.show()