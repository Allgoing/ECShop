import smtplib
import traceback
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EMail:

    def __init__(self, smtp_addr, from_addr, from_pwd, to_addrs, file_path, mail_title, to_addrs_cc=None):
        self._smtp_addr = smtp_addr
        self._from_addr = from_addr
        self._from_pwd = from_pwd
        self._to_addrs = to_addrs
        self._to_addrs_cc = to_addrs_cc
        self._file_path = file_path
        self._mail_title = mail_title

    def send_mail(self):
        """设置邮件头"""
        msg = MIMEMultipart()
        msg['Subject'] = self._mail_title
        msg['From'] = self._from_addr
        msg['To'] = self._to_addrs
        msg['Cc'] = self._to_addrs_cc
        msg.attach(MIMEText('测试报告见附件。', 'plain', 'utf-8'))

        with open(self._file_path, 'rb') as fp:
            '''添加附件'''
            try:
                fp_part = MIMEApplication(fp.read())
                fp_part.add_header('Content-Disposition', 'attachment', filename='index.html')
                fp_part.add_header('Content-ID', '<0>')
                fp_part.add_header('X-Attachment-Id', '0')
                msg.attach(fp_part)
            except Exception:
                print('文件不存在')
                print(traceback.print_exc())

        try:
            server = smtplib.SMTP_SSL(self._smtp_addr, 465)
            # server.set_debuglevel(1)
            server.login(self._from_addr, self._from_pwd)
            if self._to_addrs_cc is None:
                server.sendmail(self._from_addr, self._to_addrs.split(','), msg.as_string())
            else:
                server.sendmail(self._from_addr, (self._to_addrs+','+self._to_addrs_cc).split(','), msg.as_string())
            server.quit()
        except Exception:
            print("邮件发送失败")
            print(traceback.print_exc())
#
#
# if __name__ == '__main__':
#     mail_title = '自动化测试平台 Test Report    【此邮件为系统自动发送，请勿回复】'
#     a = EMail('smtp.qq.com', '3162909642@qq.com', 'hdvnaxyzhdcmddca', 'lihang1988@126.com,573447533@qq.com',
#               r'E:\report\index.html', mail_title, '750583646@qq.com')
#     a.send_mail()
