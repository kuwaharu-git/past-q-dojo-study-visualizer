import pandas as pd
from matplotlib import pyplot as plt
import japanize_matplotlib
from encode_csv import encode

encode()
data = pd.read_csv("report.csv", encoding="utf-8")

day_data = {}

for index, row in data.iterrows():
    if not row["学習日"] in day_data:
        day_data[row["学習日"]] = [0, 0]
    if row["正誤"] == "○":
        day_data[row["学習日"]][0] += 1
    else:
        day_data[row["学習日"]][1] += 1

# 折れ線グラフのデータ
x = list(day_data.keys())
y = [sum(list(day_data.values())[0])]
for i in range(1, len(list(day_data.values()))):
    y.append(sum(list(day_data.values())[i]) + y[-1])

y_1 = [list(day_data.values())[0][0]]
for i in range(1, len(list(day_data.values()))):
    y_1.append(list(day_data.values())[i][0] + y_1[-1])

y_2 = [list(day_data.values())[0][1]]
for i in range(1, len(list(day_data.values()))):
    y_2.append(list(day_data.values())[i][1] + y_2[-1])

# 棒グラフのデータ
y_a = [day_data[day][0] for day in x]  # 正解数
y_b = [day_data[day][1] for day in x]  # 間違い数

# グラフの描画
plt.figure(figsize=(len(x), y[-1]//50))   # 描画サイズ

# 折れ線グラフの描画
plt.plot(x, y, label="all", marker='o', color='blue')
plt.plot(x, y_1, label="True", marker='o', color='green')
plt.plot(x, y_2, label="False", marker='o', color='red')

# 棒グラフの描画
plt.bar(x, y_a, color='green', width=-0.35, edgecolor='grey', align='edge', label='True')
plt.bar(x, y_b, color='red', width=0.35, edgecolor='grey', align='edge', label='False')

# ラベルと凡例の設定
plt.xlabel('学習日', fontsize=12)
plt.ylabel('数', fontsize=12)
plt.title('学習日ごとの正解と間違いの数', fontsize=14)
plt.legend()

# グラフの表示
plt.tight_layout()
plt.show()
