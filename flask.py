"""
from:表示从什么地方导包
import:导入一个叫做Flask的包,Flask是大写
"""
from flask import Flask
# import xxxxx
"""
在公司进行开发的时候:
学习一门新技术:
1 通过百度学习
2 通过源码学习
3 通过官方文档学习
"""
"""
__name__:有两个意思
1 表示main函数(入口函数)__main__
2 如果做为模块导入,就是模块的名字
"""

"""
创建一个flask的应用程序,名字叫做app
语法: flask对象的名字 = Flask(__name__)
__name__:表示模块名字
"""
app = Flask(__name__)
"""
@app.route("/"):通过装饰器,设置请求的路由(URL地址),或者在JAVA里面也叫做接口
语法:@flask对象的名字.route("/"),
注意:app是对象的名字,名字可以随意取
@app.route("/"):参数必须义斜线开头
def index():def 表示定义一个函数,index表示函数的名字,函数名字可以随意取
"""

@app.route("/baidu")
def index():
    # 写我们的业务逻辑
    # return:表示渲染(展示)页面
    return "我是百度的页面"

# 表示入口函数
# if __name__ == '__main__':表示语法,固定的写法
if __name__ == '__main__':
    # 启动应用程序
    app.run()