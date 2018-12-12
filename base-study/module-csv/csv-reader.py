"""
读取csv文件的两种方法
"""
import csv


def read_csv_demo1():
    with open('./student.csv', 'r') as fp:
        # 这种方式读取所有的内容，包含头信息
        reader = csv.reader(fp)
        next(reader)
        for line in reader:
            print(line)


def read_csv_demo2():
    with open('./student.csv', 'r') as fp:
        # DictReader读取的内容不包含头信息
        reader = csv.DictReader(fp)
        for line in reader:
            print(line['name'])


if __name__ == '__main__':
    read_csv_demo1()
