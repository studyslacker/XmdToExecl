users=[{"name":"张三"}]


def regin(username, password):
    for i in users:
        if username == i["name"]
            print("用户名已存在")
            else:
            print("注册成功")


    return None


def login(username, password):
    if username & password:
        for i in users:
            if username == i["name"] & & password == i["password"]
                print("登录成功")
                else:
                print("用户名或密码错误，请重新输入")

            else:
                print("请输入用户名或密码")
    return None

if __name__ == '__main__':
   path=r"C:\pythonProject1\com\myproject\file\测试用例.xmind"
   print(getXmind(path))