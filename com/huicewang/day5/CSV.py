import csv
import traceback
# 1.工具类 ----解析csv文件
# 2.实例化，需要传入一个参数，csv文件路径
# 3.方法：
#     1.返回csv文件的全部内容（字典形式）
#     2.根据传入的行号和列名，返回制定单元的内容（字符串） 1，‘name’
#     3.根据传入列名返回整列的内容（数组）


class CSV:

    def __init__(self, file_path):
        self.file_path = file_path
        self.my_rows = None
        try:
            with open(self.file_path) as csv_file:
                rows = csv.DictReader(csv_file)
                self.my_rows = [dict(row) for row in rows]
        except:
            traceback.print_exc()

    def get_all(self):
        return self.my_rows

    def get_cell(self, row_number, column_name):
        result = None
        if row_number > 0:
            try:
                result = self.my_rows[row_number-1][column_name]
            except:
                print('列名不存在')
        else:
            print('行号从1开始')

        return result

    def get_column(self, name):
        name_list = []
        try:
            for row in self.my_rows:
                name_list.append(row[name])
        except:
            traceback.print_exc('列名不存在')

        return name_list

    def write(self, data):
        with open(self.file_path, 'a+', newline='') as csv_file:
            csv.writer(csv_file).writerows(data)

if __name__ == '__main__':
    demo = CSV('./student.csv')
    # a = demo.get_all()
    # b = demo.get_cell(3, 'name')
    # c = demo.get_column('age')
    data = [['4', 'zhangsan', '20'], ['5', 'lisi', '44']]
    demo.write(data)
