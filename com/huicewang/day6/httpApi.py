import requests

from com.huicewang.day6.ExcelParser import ExcelParser


class HttpApi(object):

    def __init__(self, excel_path):
        self.ep = ExcelParser(excel_path)

    def do_get(self, url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params).json()

    def get_url(self, sheet, row_name, row_num=0, col_num=2, col_name='接口地址'):
        interface_url = ''
        row_index = self.ep.get_row_index(sheet, col_num, row_name)
        col_index = self.ep.get_col_index(sheet, row_num, col_name)
        interface_url = self.ep.get_cell(sheet, row_index, col_index)
        return interface_url

if __name__ == '__main__':
    ha = HttpApi(r'G:\接口用例.xlsx')
    a = ha.get_url('名称', 'GetAuthService')
    print(a)