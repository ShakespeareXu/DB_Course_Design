from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox
import pymssql
from PySide2.QtWidgets import QTableWidgetItem

class BaseDAO:
    def __init__(self):
        self.connection = pymssql.connect(
            server='127.0.0.1',  # 或您的数据库服务器地址
            user='sa',  # 您的数据库用户名
            password='123456',  # 您的数据库密码
            database='plant',  # 您的数据库名称
            charset='UTF-8',
            tds_version="7.0"
        )
        self.cursor = self.connection.cursor(as_dict=True)

class UserDAO(BaseDAO):
    def get_all_manager_users(self):
        super().__init__()
        print("内层也被点击了")
        query = "SELECT * FROM 上级主管部门"
        self.cursor.execute(query)
        users = []
        rows = self.cursor.fetchall()
        for row in rows:
            user = {
                "用户名": row["用户名"],
                "密码": row["密码"]
            }
            users.append(user)
        return users
    def get_all_converse_users(self):
        super().__init__()
        print("内层也被点击了")
        query = "SELECT * FROM 养护人员"
        self.cursor.execute(query)
        users = []
        rows = self.cursor.fetchall()
        for row in rows:
            user = {
                "用户名": row["用户名"],
                "密码": row["密码"]
            }
            users.append(user)
            print(user)
        return users
    def get_all_monitor_users(self):
        super().__init__()
        print("内层也被点击了")
        query = "SELECT * FROM 监测人员"
        self.cursor.execute(query)
        users = []
        rows = self.cursor.fetchall()
        for row in rows:
            user = {
                "用户名": row["用户名"],
                "密码": row["密码"]
            }
            users.append(user)
        return users
    




class PlantInfoWindow():
    def __init__(self):
        self.window = QUiLoader().load("ui/PlantInfo.ui")

class AccountWindow(UserDAO):
    def __init__(self):
        self.window = QUiLoader().load("ui/Account.ui")
        self.window.manager_users_button.clicked.connect(self.show_all_manager_users)
        self.window.converse_user_button.clicked.connect(self.show_all_converse_users)
        self.window.monitor_user_button.clicked.connect(self.show_all_monitor_users)

    def show_all_manager_users(self):
        users = self.get_all_manager_users()
        print("窗口按钮被点击")
        print(users)
        # 清除表格现有内容
        self.window.user_password_show.setRowCount(0)
        # 设置表格列数
        self.window.user_password_show.setColumnCount(2)
        # 设置表格的列标题
        self.window.user_password_show.setHorizontalHeaderLabels(['用户名', '密码'])
        # 遍历用户列表，将每个用户的信息添加到表格中
        for user in users:
            row = self.window.user_password_show.rowCount()
            self.window.user_password_show.insertRow(row)
            self.window.user_password_show.setItem(row, 0, QTableWidgetItem(user['用户名']))
            self.window.user_password_show.setItem(row, 1, QTableWidgetItem(user['密码']))

    def show_all_converse_users(self):
        users = self.get_all_converse_users()
        print("窗口按钮被点击")
        print(users)
        # 清除表格现有内容
        self.window.user_password_show.setRowCount(0)
        # 设置表格列数
        self.window.user_password_show.setColumnCount(2)
        # 设置表格的列标题
        self.window.user_password_show.setHorizontalHeaderLabels(['用户名', '密码'])
        # 遍历用户列表，将每个用户的信息添加到表格中
        for user in users:
            row = self.window.user_password_show.rowCount()
            self.window.user_password_show.insertRow(row)
            self.window.user_password_show.setItem(row, 0, QTableWidgetItem(user['用户名']))
            self.window.user_password_show.setItem(row, 1, QTableWidgetItem(user['密码']))

    def show_all_monitor_users(self):
        users = self.get_all_monitor_users()
        print("窗口按钮被点击")
        print(users)
        # 清除表格现有内容
        self.window.user_password_show.setRowCount(0)
        # 设置表格列数
        self.window.user_password_show.setColumnCount(2)
        # 设置表格的列标题
        self.window.user_password_show.setHorizontalHeaderLabels(['用户名', '密码'])
        # 遍历用户列表，将每个用户的信息添加到表格中
        for user in users:
            row = self.window.user_password_show.rowCount()
            self.window.user_password_show.insertRow(row)
            self.window.user_password_show.setItem(row, 0, QTableWidgetItem(user['用户名']))
            self.window.user_password_show.setItem(row, 1, QTableWidgetItem(user['密码']))

    

class AdminitratorWindow():
    plant_info_window = None
    plant_classify_window = None
    account_window = None

    def __init__(self):
        self.window = QUiLoader().load("ui/Administrator.ui")
        self.window.plant_info_button.clicked.connect(self.get_plant_info_window)
        self.window.plant_classify_button.clicked.connect(self.get_plant_classify_window)
        self.window.account_button.clicked.connect(self.get_account_window)
    def get_plant_info_window(self):
        if not AdminitratorWindow.plant_info_window:
            AdminitratorWindow.plant_info_window = PlantInfoWindow()
        AdminitratorWindow.plant_info_window.window.show()
    def get_plant_classify_window(self):
        pass
    def get_account_window(self):
        if not AdminitratorWindow.account_window:
            AdminitratorWindow.account_window = AccountWindow()
        AdminitratorWindow.account_window.window.show()

class LoginWindow(BaseDAO):
    admin_window = None

    def __init__(self):
        super().__init__()
        str = "连接失败！"
        if self.connection:
            str = '连接成功！'
        print(str)
        # 封装文件对象
        self.window = QUiLoader().load("ui/Login.ui")
        self.window.login_button.clicked.connect(self.login)


    def login(self):
        identity = self.window.identity_cbox.currentText()
        username = self.window.logname_ledit.text()
        password = self.window.password_ledit.text()

        if username == "" or password == "":
            QMessageBox.warning(self.window, "登录失败", "用户名或密码不可为空！")
        else:
            if identity == "系统管理员":
                # 验证plant数据库中[系统管理员]表的[用户名]列和[密码]列的内容与username和password是否一致
                query = f"SELECT [密码] FROM [系统管理员] WHERE [用户名] = '{username}' AND [密码] = '{password}'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                if result:
                    QMessageBox.information(self.window, "登录成功", "登录成功！")
                    self.window.close()  # 关闭当前登录窗口
                    if not LoginWindow.admin_window:
                        LoginWindow.admin_window = AdminitratorWindow()
                    LoginWindow.admin_window.window.show()
                else:
                    QMessageBox.warning(self.window, "登录失败", "用户名或密码错误！")
            if identity == "上级主管部门":
                # 验证plant数据库中[上级主管部门]表的[用户名]列和[密码]列的内容与username和password是否一致
                query = f"SELECT [密码] FROM [上级主管部门] WHERE [用户名] = '{username}' AND [密码] = '{password}'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                if result:
                    QMessageBox.information(self.window, "登录成功", "登录成功！")
                else:
                    QMessageBox.warning(self.window, "登录失败", "用户名或密码错误！")
            if identity == "养护人员":
                # 验证plant数据库中[养护人员]表的[用户名]列和[密码]列的内容与username和password是否一致
                query = f"SELECT [密码] FROM [养护人员] WHERE [用户名] = '{username}' AND [密码] = '{password}'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                if result:
                    QMessageBox.information(self.window, "登录成功", "登录成功！")
                else:
                    QMessageBox.warning(self.window, "登录失败", "用户名或密码错误！")
            if identity == "监测人员":
                # 验证plant数据库中[监测人员]表的[用户名]列和[密码]列的内容与username和password是否一致
                query = f"SELECT [密码] FROM [监测人员] WHERE [用户名] = '{username}' AND [密码] = '{password}'"
                self.cursor.execute(query)
                result = self.cursor.fetchone()
                if result:
                    QMessageBox.information(self.window, "登录成功", "登录成功！")
                else:
                    QMessageBox.warning(self.window, "登录失败", "用户名或密码错误！")

app = QApplication([])
login = LoginWindow()
login.window.show()
app.exec_()
