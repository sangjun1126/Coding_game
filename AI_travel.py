import pandas as pd
import requests
from io import StringIO

# 데이터 다운로드
urls = [
    "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_travel_%E1%84%8B%E1%85%A7%E1%84%92%E1%85%A2%E1%86%BC_A.csv",
    "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_traveller_master_%E1%84%8B%E1%85%A7%E1%84%92%E1%85%A2%E1%86%BC%E1%84%80%E1%85%A2%E1%86%A8%20Master_A.csv",
    "https://raw.githubusercontent.com/kairess/toy-datasets/master/tn_visit_area_info_%E1%84%87%E1%85%A1%E1%86%BC%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%B5%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%87%E1%85%A9_A.csv"
]

dfs = []

for url in urls:
    response = requests.get(url)
    content = response.content.decode("utf-8")
    df = pd.read_csv(StringIO(content))
    dfs.append(df)

# 각각의 데이터프레임을 변수로 저장
travel_df, traveller_master_df, visit_area_info_df = dfs

print(travel_df.head())
