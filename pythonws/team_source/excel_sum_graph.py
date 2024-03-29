import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image 
import os
import re
import smtplib

file_format = ".xlsx"  # or ".csv"
file_path = r'D:\gwonys\workspace\pythons'
file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]

merge_df = pd.DataFrame()
filename = "병합파일.xlsx"


for file_name in file_list:
    file_df = pd.read_excel(file_name)
    temp_df = pd.DataFrame(file_df)
    merge_df = pd.concat([merge_df, file_df], ignore_index=True)
    
merge_df.to_excel(filename , index=False)

data = pd.read_excel(filename)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

price = data['가격'].sort_values(ascending=True)
axes[0].scatter(x=range(len(price)), y=price)
axes[0].set_xlabel('권 수')
axes[0].set_ylabel('가격')
axes[0].set_title('소설() 가격')

# Convert '발행일' to datetime format
data['발행일'] = pd.to_datetime(data['발행일'], errors='coerce')

# Extract only the year from the '발행일' column
data['연도'] = data['발행일'].dt.year

sns.countplot(x='연도', data=data, ax=axes[1])
axes[1].set_xlabel('연 도')
axes[1].set_ylabel('권 수')
axes[1].set_title('소설() 발행일')

plt.tight_layout()
plt.savefig('그래프.jpg',format='jpeg')

load_xlsx = load_workbook(os.path.join(file_path,filename))
load_sheet = load_xlsx.active
img = Image('그래프.jpg')
load_sheet.add_image(img,'F1')
load_xlsx.save(filename)