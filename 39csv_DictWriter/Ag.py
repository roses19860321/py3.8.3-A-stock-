import csv

headers = ['name', 'age']

datas = [{'name':'Bob', 'age':23},
        {'name':'Jerry', 'age':44},
        {'name':'Tom', 'age':15}
        ]

with open('example.csv', 'w', newline='') as f:
    # 标头在这里传入，作为第一行数据
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    for row in datas:
        writer.writerow(row)