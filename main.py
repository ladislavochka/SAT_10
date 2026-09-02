import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("C:/Users/Logika/Desktop/Logika/SAT_10-2-3-main/Task2/apps_clean.csv")
count = df["Content Rating"].value_counts().head(5)
plt.pie(count, labels=count.index, autopct = '%1.1f%%')
plt.title("Категорії застосунків за віком")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["Rating"].dropna(), bins = 15)
plt.title("Розподіл рейтингу застосунків")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xlim(0, 5) #обмеження осі х 
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(df["Rating"], df["Installs"])
plt.title("Залежність завантажувань від рейтингу")
plt.xlabel("Rating")
plt.ylabel("Installs")
plt.show()