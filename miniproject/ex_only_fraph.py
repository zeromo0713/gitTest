import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일을 Pandas DataFrame으로 읽기
file_path = '책리스트.csv'
df = pd.read_csv(file_path)

# '가격' 컬럼을 숫자로 변환 (천 단위 쉼표 제거)
df['가격'] = df['가격'].replace('[\$,]', '', regex=True).astype(float)

# '가격대' 컬럼을 추가하여 가격대별로 그룹화
bins = [0, 5000, 10000,15000, 20000, float('inf')]  # 가격대 구간 설정
labels = ['0-5000', '5000-10000', '10000-15000','15000-20000', '20000+']
df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels, right=False)

# 가격대별 빈도를 막대 그래프로 시각화
price_groups = df.groupby('가격대').size()
price_groups.plot(kind='bar', color='skyblue')
plt.title('가격대별 상품 수')
plt.xlabel('가격대')
plt.ylabel('상품 수')
plt.show()
