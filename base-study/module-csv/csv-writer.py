"""
csv写入的两种方法
"""
import csv


def writer_csv_demo1():
    """
    数据以数组的形式展现
    :return:
    """
    header = ['name', 'age', 'address', 'grade']
    infos = [
        ['rose', 12, '中国', 1],
        ['rose', 13, '中国', 2],
        ['jark', 14, '美国', 3],
        ['tom', 15, '中国', 4]
    ]
    with open('./test.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(infos)


def writer_csv_demo2():
    """
    数据以字典的形式展现
    :return:
    """
    header = ['name', 'age', 'address', 'grade']
    infos = [
        {'name': 'rose', 'age': 12, 'address': '中国', 'grade': 1},
        {'name': 'tom', 'age': 12, 'address': '美国', 'grade': 2}

    ]
    with open('./test2.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, header)
        writer.writeheader()
        writer.writerows(infos)


if __name__ == '__main__':
    writer_csv_demo2()
