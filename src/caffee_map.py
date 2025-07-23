import pandas as pd

# 데이터 불러오기
area_map = pd.read_csv('./data/area_map.csv') # 건설 현장 위치 (0: 없음, 1: 있음)
area_struct = pd.read_csv('./data/area_struct.csv') # 지역별 구조물 위치 (category 0: 없음, 1~4: 있음)
area_category = pd.read_csv('./data/area_category.csv', sep=', ') # 구조물의 카테고리(숫자) 정의

# 데이터 출력
print("✅ area_map DataFrame:\n", area_map.head())
print("✅ area_struct DataFrame:\n", area_struct.head())
print("✅ area_category DataFrame:\n", area_category.head())

# 세 개의 데이터 파일을 하나의 DataFrame으로 병합
merged_map_struct = pd.merge(area_map, area_struct, on=['x', 'y'], how='inner') # 공통적으로 존재하는 요소들만 병합
df_final = pd.merge(merged_map_struct, area_category, on='category', how='left') # category 기준 left에 right 병합 (left에만 있는 건 NaN 처리)

# 정렬 및 필터링
df_final = df_final.sort_values('area') # area 기준 오름차순 정렬
df_final_area1 = df_final[df_final['area'] == 1] # area 1 지역만 필터링

# 결과 출력
print("✅ df_final_area1 DataFrame:\n", df_final_area1)

struct_category_counts = df_final[['category', 'struct']].value_counts()
print("✅ 각 구조물(struct)의 개수:\n", struct_category_counts)

overlap = df_final.loc[
    (df_final['ConstructionSite'] == 1) & 
    (df_final['category'] != 0)
]
print("✅ 건설 현장과 구조물이 겹치는 곳:\n", overlap)
