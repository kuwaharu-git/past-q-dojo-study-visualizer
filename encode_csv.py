import chardet
import pandas as pd


def encode():
    # ファイル名
    input_file = input("ファイル名の入力")
    output_file = "report.csv"

    # 1. 文字エンコーディングを自動検出
    with open(input_file, 'rb') as f:
        result = chardet.detect(f.read())

    # 検出されたエンコーディング
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

    # 2. 検出されたエンコーディングでファイルを読み込み
    data = pd.read_csv(input_file, encoding=encoding)

    # 3. UTF-8で新しいファイルに保存
    data.to_csv(output_file, encoding='utf-8', index=False)
