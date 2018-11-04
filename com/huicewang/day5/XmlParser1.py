import traceback
import xml.etree.ElementTree as ET


class XmlParser:

    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.root = ET.parse(file_path)
        except:
            print('待解析文件加载异常'+traceback.print_exc())
            self.root = None

    def get_element_text(self, xpath):
        result = None
        if self.root is not None:
            try:
                element = self.root.find(xpath)
                result = element.text
            except:
                print('对象没有找到:'+xpath)
                # traceback.print_exc()
        return result

    def get_element_attribute(self, xpath, name):
        result = None
        if self.root is not None:
            try:
                element = self.root.find(xpath)
                result = element.attrib[name]
            except:
                print('对象没有找到:'+xpath)
                # traceback.print_exc()
        return result


if __name__ == '__main__':
    demo = XmlParser('./config.xml')
    print(demo.get_element_attribute('.//首页/登录按钮', 'type'))
    print(demo.get_element_attribute('.//首页/登录按钮', 'value'))
    print(demo.get_element_attribute('.//登录页/密码', 'type'))
    print(demo.get_element_attribute('.//登录页/密码', 'value'))
