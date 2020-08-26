import pandas as pd


# CSVファイルを読み込む
df = pd.read_csv('test.csv')

# 1行のデータを表示
print('Cのデータ\n', df.loc[2])

# 複数の行のデータを表示
print('CとDのデータ\n', df.loc[[2,3]])

# 指定した行の指定した列のデータを表示
print('Cの国語のデータ', df.loc[2]['国語'])