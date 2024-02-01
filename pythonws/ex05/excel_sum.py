import pandas as pd
import os
import matplotlib.pyplot as plt
from io import BytesIO
import openpyxl

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 'io.excel.zip.reader' 설정 초기화
# pd.reset_option('io.excel.zip.reader', silent=True)

# 합칠 엑셀 파일들이 있는 폴더 경로
folder_path = r'E:\zeromo\workspace\pythonws'

# 결과를 저장할 엑셀 파일 이름
output_excel_name = '결과파일.xlsx'

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

                # 그래프 생성
                plt.bar(current_sheet_df['가격대'], current_sheet_df['상품 수'])
                plt.title('가격대별 상품 수')
                plt.xlabel('가격대')
                plt.ylabel('상품 수')

                # 그래프를 이미지로 저장
                image_stream = BytesIO()
                plt.savefig(image_stream, format='png')
                plt.close()

                # BytesIO에서 파일로 저장 (그래프 이미지 파일명은 원하는 대로 지정)
                graph_image_path = f'그래프_{sheet_output_name}.png'
                with open(graph_image_path, 'wb') as img_file:
                    img_file.write(image_stream.read())

                # 이미지를 엑셀에 추가
                image_sheet = writer.sheets[sheet_output_name]
                img = openpyxl.drawing.image.Image(graph_image_path)
                img.width = 400  # 이미지의 가로 크기 조정
                img.height = 300  # 이미지의 세로 크기 조정
                image_sheet.add_image(img, 'K2')  # 이미지를 K2 셀에 삽입
