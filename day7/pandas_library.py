import pandas as pd     #as keyword to short the library name

#to read csv files
csv_path = "./file.csv"

df = pd.read_csv(csv_path)

print(df)
df.head()

#to read xlsx(excel) files
xlsx_path = "./file.csv"

df = pd.read_excel(xlsx_path)

print(df)
df.head()