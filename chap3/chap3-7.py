import pandas as pd


# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 条件に合うデータを抽出する
data_s = df[df['国語'] >= 90]
print('国語の点数が90点以上\n', data_s)

data_c = df[df['数学'] < 70]
print('数学の点数が70点以下\n', data_c)
