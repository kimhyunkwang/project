import matplotlib.pyplot as plt
import caffee_map

# 조건에 맞는 데이터프레임 정의하기
df = caffee_map.df_final
construction_site = df[df['ConstructionSite'] == 1]
apartment_building = df.loc[(df['ConstructionSite'] == 0) & (df['struct'].isin(['Apartment', 'Building']))] # 건설 현장과 겹치지 않는 아파트, 빌딩
bandalgom_coffee = df[df['struct'] == 'BandalgomCoffee']
my_home = df[df['struct'] == 'MyHome']

# 그래프 사이즈 변경
plt.figure(figsize=(6, 6))

# 좌측 상단 (1, 1), 우측 하단 (15, 15)
plt.xlim(0, 16)
plt.ylim(0, 16)
plt.gca().invert_yaxis() # y축 방향 반전

# 눈금 간격 1로 변경(x, y축 모두)
plt.xticks(range(1, 16))
plt.yticks(range(1, 16))

# 그리드 그리기(점선)
plt.grid(linestyle = ':')

# 구조물 위치 표시하기
plt.scatter(construction_site['x'], construction_site['y'], c='gray', marker='s', s=200, label='Construction Site')
plt.scatter(apartment_building['x'], apartment_building['y'], c='brown', marker='o', s=200, label='Apartment/Building')
plt.scatter(bandalgom_coffee['x'], bandalgom_coffee['y'], c='green', marker='s', s=200, label='Bandalgom Coffee')
plt.scatter(my_home['x'], my_home['y'], c='green', marker='^', s=200, label='My Home')

# 축 레이블, 범례 추가
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(fontsize=8, markerscale=0.5) # markerscale: 기존 마커의 몇 배로 설정할지

# 이미지 저장
plt.savefig('./result/map.png')

# 차트 표시
plt.show()
