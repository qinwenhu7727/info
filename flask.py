"""
from:��ʾ��ʲô�ط�����
import:����һ������Flask�İ�,Flask�Ǵ�д
"""
from flask import Flask
# import xxxxx
"""
�ڹ�˾���п�����ʱ��:
ѧϰһ���¼���:
1 ͨ���ٶ�ѧϰ
2 ͨ��Դ��ѧϰ
3 ͨ���ٷ��ĵ�ѧϰ
"""
"""
__name__:��������˼
1 ��ʾmain����(��ں���)__main__
2 �����Ϊģ�鵼��,����ģ�������
"""

"""
����һ��flask��Ӧ�ó���,���ֽ���app
�﷨: flask��������� = Flask(__name__)
__name__:��ʾģ������
"""
app = Flask(__name__)
"""
@app.route("/"):ͨ��װ����,���������·��(URL��ַ),������JAVA����Ҳ�����ӿ�
�﷨:@flask���������.route("/"),
ע��:app�Ƕ��������,���ֿ�������ȡ
@app.route("/"):����������б�߿�ͷ
def index():def ��ʾ����һ������,index��ʾ����������,�������ֿ�������ȡ
"""

@app.route("/baidu")
def index():
    # д���ǵ�ҵ���߼�
    # return:��ʾ��Ⱦ(չʾ)ҳ��
    return "���ǰٶȵ�ҳ��"

# ��ʾ��ں���
# if __name__ == '__main__':��ʾ�﷨,�̶���д��
if __name__ == '__main__':
    # ����Ӧ�ó���
    app.run()