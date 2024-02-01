import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd

# import seaborn as sns

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False



# CSV 파일을 Pandas DataFrame으로 읽기
file_path = '책리스트.csv'
df = pd.read_csv(file_path)

# '가격' 컬럼을 숫자로 변환 (천 단위 쉼표 제거)
df['가격'] = df['가격'].replace('[\$,]', '', regex=True).astype(float)

# '가격대' 컬럼을 추가하여 가격대별로 그룹화
bins = [0, 5000, 10000,15000, 20000, float('inf')]  # 가격대 구간 설정
labels = ['0-5000', '5000-10000', '10000-15000','15000-20000', '20000+']
df['가격대'] = pd.cut(df['가격'], bins=bins, labels=labels, right=False)

# 한글 폰트 설정
# font_path = r'C:\Users\user\Desktop\빵모\한글 폰트\나눔 글꼴\나눔고딕\NanumFontSetup_TTF_GOTHIC\NanumGothic.ttf'  # 자신의 한글 폰트 경로로 바꿔주세요.
# font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family='sans-serif')

# 가격대별 빈도를 막대 그래프로 시각화
price_groups = df.groupby('가격대').size()
price_groups.plot(kind='bar', color='skyblue')
plt.title('가격대별 상품 수')
plt.xlabel('가격대')
plt.ylabel('상품 수')

# 그래프에 추가 설명 넣기
plt.text(0.5, -0.1, '가격대별로 분류된 상품의 수를 나타낸 그래프입니다.', ha='center', va='center', transform=plt.gca().transAxes)


plt.show()

