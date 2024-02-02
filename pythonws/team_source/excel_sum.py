import pandas as pd
from openpyxl import Workbook
import os

file_format = ".xlsx"  # or ".csv"
file_path = r'D:\zeromo\workspace\pythonws'
file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]

merge_df = pd.DataFrame()

for file_name in file_list:
    file_df = pd.read_excel(file_name)
    merge_df = pd.concat([merge_df, file_df], ignore_index=True)

# 파일 한 번만 저장
merge_df.to_excel("병합파일.xlsx", index=False)
