import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import openpyxl
import re
import warnings

# 경고 메시지 무시 설정      ====> 경고가 계속 나와서 일단 무시하고 넘어가기 위해서 적용해보았으요
# warnings.simplefilter(action='ignore', category=FutureWarning)

# 그래프에 한글이 깨지는 것을 방지해줌   ==> 그래프에 한글이 깨지면 글씨 부분이 ㅁㅁ이런식으로 네모로 나와버린다
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# CSV 또는 엑셀 파일을 Pandas DataFrame으로 읽기
file_path = '통합파일.xlsx'
# sheet_name=None으로 설정하여 모든 시트를 읽습니다.
df_dict = pd.read_excel(file_path, sheet_name=None)

# 엑셀 파일에 이미지 추가
#위 코드에서는 mode='a'로 설정하여 기존 엑셀 파일에 이미지를 추가합니다. 또한 writer.book을 사용하지 않고 excel_writer.sheets를 직접 활용하여 이미지를 추가합니다
with pd.ExcelWriter(file_path, engine='openpyxl', mode='a') as excel_writer:
    for sheet_name, df in df_dict.items():
        # '가격' 컬럼을 숫자로 변환 (천 단위 쉼표 제거)
        df['가격'] = df['가격'].replace(r'[\$,]', '', regex=True).astype(float)

        # '가격대' 컬럼을 추가하여 가격대별로 그룹화
        bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, float('inf')]  # 가격대 구간 설정
        labels = ['0-5000', '5000-10000', '10000-15000', '15000-20000', '20000-25000', '25000-30000', '30000+']
        df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels, right=False)

        # 가격대별 빈도를 막대 그래프로 시각화
        price_groups = df.groupby('가격대').size()

        # 그래프 설정
        fig, ax = plt.subplots()
        ax.bar(price_groups.index, price_groups.values, color='skyblue')

        # 그래프에 추가 설명 넣기
        ax.set_title(f'{sheet_name} - 가격대별 상품 수')  # 그래프 제목
        ax.set_xlabel('가격대')  # x축 레이블
        ax.set_ylabel('상품 수')  # y축 레이블

        # 가격대 별 권수 표시
        for i, v in enumerate(price_groups.values):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom')

        # 총 권수 표시
        total_books = price_groups.sum()
        ax.text(len(price_groups) / 2, max(price_groups.values) + 1, f'총 권수: {total_books}', ha='center', va='bottom')

        # 그래프를 이미지로 저장
        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        plt.close()

        # BytesIO에서 파일로 저장
        image_stream.seek(0)
        
        # 특수문자 제거하여 시트 이름 정의
        clean_sheet_name = re.sub(r'\W+', '', sheet_name)
        
        image_path = f'{clean_sheet_name}_그래프.png'
        with open(image_path, 'wb') as img_file:
            img_file.write(image_stream.read())

        # 이미지 삽입
        img = openpyxl.drawing.image.Image(image_stream)
        img.width = 400  # 이미지의 가로 크기 조정
        img.height = 300  # 이미지의 세로 크기 조정
        img.anchor = 'K2'  # 이미지를 원하는 위치에 삽입
        img.title = f'{sheet_name}_그래프'  # 이미지 제목 설정
        excel_writer.sheets[clean_sheet_name].add_image(img)
