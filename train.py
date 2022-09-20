import os
import zipfile
import wget
import config
import pandas as pd

path = "deu-eng.zip"
data_path = "deu.txt"

if "deu.txt" not in os.listdir():
    zip_ref = zipfile.ZipFile(path)
    zip_ref.extractall()
    zip_ref.close()

# Read the data
df = pd.read_table(data_path,names=['source', 'target', 'comments'])
df = df.drop("comments",axis=1)

print(df.head())
print(len(df))