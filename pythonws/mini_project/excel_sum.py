import pandas as pd
import os

# 'io.excel.zip.reader' 설정 초기화
# pd.reset_option('io.excel.zip.reader', silent=True)

# 합칠 엑셀 파일들이 있는 폴더 경로
folder_path = r'D:\zeromo\workspace\pythonws'

# 결과를 저장할 엑셀 파일 이름
output_excel_name = '통합파일.xlsx'

# 폴더 내 모든 파일에 대해 반복
with pd.ExcelWriter(output_excel_name, engine='xlsxwriter') as writer:
    for file_name in os.listdir(folder_path):
        # 파일 확장자가 .xlsx인 경우에만 진행
        if file_name.endswith('.xlsx'):
            # 엑셀 파일을 읽어옴
            current_excel_path = os.path.join(folder_path, file_name)

            # 엑셀 파일의 시트 이름들을 수동으로 추출
            excel_sheets = pd.read_excel(current_excel_path, sheet_name=None).keys()

            # 엑셀 파일의 각 시트에 대해 반복
            for sheet_name in excel_sheets:
                # 시트를 데이터프레임으로 읽어옴
                current_sheet_df = pd.read_excel(current_excel_path, sheet_name=sheet_name)

                # 시트의 이름을 현재 파일의 이름과 결합하여 저장
                sheet_output_name = f"{file_name}_{sheet_name}"
                current_sheet_df.to_excel(writer, sheet_name=sheet_output_name, index=False)

                