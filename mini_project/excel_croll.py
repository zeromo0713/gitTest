import os
import time
import pandas as pd
import openpyxl
import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
# 합칠 엑셀 파일 이름
output_excel_name = '통합파일.xlsx'

# 폴더 내 모든 CSV(확장파일) 파일에 대해 반복
csv_folder_path =  r'D:\zeromo\workspace\pythonws' # ========================파일경로는 각자 경로===============================
csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]   # f.endswith('.csv')여기 부분  확장파일 csv파일 말고 xlsx등 변경 가능

with pd.ExcelWriter(output_excel_name, engine='xlsxwriter') as writer:
    for idx, csv_file in enumerate(csv_files, start=1):    # idx와 enumerate 을 붙여서 인덱스 번호를 부여해준다 ㅎ.ㅎ
        # CSV 파일을 읽어옴
        current_csv_path = os.path.join(csv_folder_path, csv_file)

        # CSV 파일을 데이터프레임으로 읽어옴
        df = pd.read_csv(current_csv_path)

        # 원하는 컬럼만 선택
        selected_columns = ['제목', '가격']
        df = df[selected_columns]

        # 엑셀 시트 이름을 현재 파일의 이름과 결합하여 저장
        sheet_name = f"시트{idx}_{os.path.splitext(csv_file)[0]}"  #여기의 시트{idx}_이 부분 때문에 특수문자 복잡해짐..
        df.to_excel(writer, sheet_name=sheet_name, index=False)


# ========================Frame 창 띄워서 이쁘게 보기============================================
# import tkinter as tk
# from tkinter import ttk
# # Tkinter 창 생성
# window = tk.Tk()
# window.title("데이터프레임 뷰어")

# # 데이터프레임을 표시할 Treeview 위젯 생성
# tree = ttk.Treeview(window)
# tree["columns"] = tuple(subset_df.columns)

# # 열 제목 설정
# for column in subset_df.columns:
#     tree.heading(column, text=column)

# # Treeview에 데이터 삽입
# for index, row in subset_df.iterrows():
#     tree.insert("", "end", values=tuple(row))

# # Treeview를 창에 적절히 배치
# tree.pack(expand=True, fill="both")

# # 행의 수를 보여줄 레이블 생성
# label = tk.Label(window, text=str(len(subset_df)) + '개')
# label.pack()

# # Tkinter 이벤트 루프 실행
# window.mainloop()

# #============================subset_df부분에는 자신이 설정한 frame 변수명 하기 ^.^=====================나는 df================
# ========================Frame 창 띄워서 이쁘게 보기============================================