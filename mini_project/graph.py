import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import openpyxl

# CSV 파일을 Pandas DataFrame으로 읽기
file_path = '책리스트.csv'
df = pd.read_csv(file_path)

# '가격' 컬럼을 숫자로 변환 (천 단위 쉼표 제거)
df['가격'] = df['가격'].replace('[\$,]', '', regex=True).astype(float)

# '가격대' 컬럼을 추가하여 가격대별로 그룹화
bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, float('inf')]  # 가격대 구간 설정
labels = ['0-5000', '5000-10000', '10000-15000', '15000-20000', '20000-25000', '25000-30000', '30000+']
df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels, right=False)

# 가격대별 빈도를 막대 그래프로 시각화
price_groups = df.groupby('가격대').size()

# 그래프 설정
plt.bar(price_groups.index, price_groups.values, color='skyblue')

# 그래프에 추가 설명 넣기
plt.title('가격대별 상품 수')  # 그래프 제목
plt.xlabel('가격대')  # x축 레이블
plt.ylabel('상품 수')  # y축 레이블

# 가격대 별 권수 표시
for i, v in enumerate(price_groups.values):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom')

# 총 권수 표시
total_books = price_groups.sum()
plt.text(len(price_groups) / 2, max(price_groups.values) + 1, f'총 권수: {total_books}', ha='center', va='bottom')

# 그래프를 이미지로 저장
image_stream = BytesIO()
plt.savefig(image_stream, format='png')
plt.close()

# 엑셀 파일에 이미지 추가
excel_writer = pd.ExcelWriter('output_file.xlsx', engine='openpyxl')
df.to_excel(excel_writer, sheet_name='original_data', index=False)

image_stream.seek(0)
image_sheet = excel_writer.sheets['original_data']

# 이미지 삽입
img = openpyxl.drawing.image.Image(image_stream)
img.width = 400  # 이미지의 가로 크기 조정
img.height = 300  # 이미지의 세로 크기 조정
image_sheet.add_image(img, 'K2')  # 이미지를 F2 셀에 삽입

excel_writer._save()
excel_writer.close()