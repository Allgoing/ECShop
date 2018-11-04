import traceback

import xlrd



class ExcelParser(object):

    def __init__(self, file_path):
        try:
            self.book = xlrd.open_workbook(file_path)
        except FileNotFoundError:
            print('没有发现待解析的文件')
            traceback.print_exc()
            self.book = None

    def get_rows(self, sheet, row_num):
        rows = []
        if self.book is not None:
            try:
                self.sheet = self.book.sheet_by_name(sheet)
                rows = self.sheet.row_values(row_num)
            except(ValueError, IndexError):
                traceback.print_exc()
        return rows

    def get_col_index(self, sheet, row_num, name):
        col_index = None
        rows = self.get_rows(sheet, row_num)
        if rows is not []:
            col_index = rows.index(name)
        return col_index

    def get_cols(self, sheet, col_num):
        cols = []
        if self.book is not None:
            try:
                self.sheet = self.book.sheet_by_name(sheet)
                cols = self.sheet.col_values(col_num)
            except(ValueError, IndexError):
                traceback.print_exc()
        return cols

    def get_row_index(self, sheet, col_num, name):
        row_index = None
        cols = self.get_cols(sheet, col_num)
        if cols is not []:
            row_index = cols.index(name)
        return row_index

    def get_cell(self, sheet_name, row_num, col_num):
        cell_value = None
        if self.book is not None:
            try:
                self.sheet = self.book.sheet_by_name(sheet_name)
                cell_value = self.sheet.cell_value(row_num, col_num)
            except(ValueError, IndexError):
                print("请检查sheet名称或单元格地址")
                traceback.print_exc()
        return cell_value

    def get_all_cells(self, sheet_name):
        cells_list = []
        if self.book is not None:
            try:
                self.sheet = self.book.sheet_by_name(sheet_name)
                row_key_name = self.sheet.row_values(0)
                for i in range(1, self.sheet.nrows):
                    cells = {}
                    cells = dict.fromkeys(row_key_name)
                    rows = self.sheet.row_values(i)
                    for row in rows:
                        for k, v in cells.items():
                            if v is None:
                                cells[k] = row
                                break
                    cells_list.append(cells)
            except (ValueError, IndexError):
                print("请检查sheet名称或单元格地址")
                traceback.print_exc()
        return cells_list

if __name__ == '__main__':
    ep = ExcelParser(r'G:\接口用例.xlsx')
    a = ep.get_rows('名称', 0)
    print(a.index('编号'))
    b = ep.get_cols('名称', 2)
    print(b.index('GetServiceData'))
    c = ep.get_col_index('名称', 0, '接口名称')
    print(c)
    d = ep.get_row_index('名称', 2, 'GetServiceData')
    print(d)
