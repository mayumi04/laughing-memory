import csv

'''
with open('text.csv', 'w', newline ='' encoding = 'utf_8') as f:
    fieldnames = ['プログラム言語', '種類', '用途']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'プログラム言語':'Java', '種類':'コンパイラ言語', '用途':'バックエンド'})
    writer.writerow({'プログラム言語':'Python', '種類':'インタプリタ言語', '用途':'AI'})
    writer.writerow({'プログラム言語':'JavaScript', '種類':'インタプリタ言語', '用途':'フロントエンド'})
'''


with open('text.csv', 'r', encoding = 'utf_8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['プログラム言語'], row['種類'], row['用途'])