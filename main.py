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

# 棒グラフの設定
bar_width = 0.35
r1 = range(len(x))
r2 = [i + bar_width for i in r1]

# グラフの描画
fig, ax = plt.subplots(figsize=(10, 5))

# 折れ線グラフの描画
ax.plot(x, y, label="all", marker='o', color='blue')
ax.plot(x, y_1, label="True", marker='o', color='green')
ax.plot(x, y_2, label="False", marker='o', color='red')

# 棒グラフの描画
ax.bar(r1, y_a, color='green', width=bar_width, edgecolor='grey', label='True')
ax.bar(r2, y_b, color='red', width=bar_width, edgecolor='grey', label='False')

# ラベルと凡例の設定
ax.set_xlabel('学習日', fontsize=12)
ax.set_ylabel('数', fontsize=12)
ax.set_title('学習日ごとの正解と間違いの数', fontsize=14)
ax.set_xticks([r + bar_width / 2 for r in range(len(x))])
ax.set_xticklabels(x, rotation=45)
ax.legend()

# グラフの表示
plt.tight_layout()
plt.show()
