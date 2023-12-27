from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication

# app = QApplication([])
# window = QUiLoader().load("ui/分布地.ui")
# window.show()
# app.exec_()

class MaintainWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("MaintenanceManagement.ui")
        self.window.detail_button.clicked.connect(self.get_detail_window)
        self.window.modify_button.clicked.connect(self.get_modify_window)
        self.window.search_button.clicked.connect(self.get_search_info)
        self.window.add_button.clicked.connect(self.put_add_info)
        self.window.delete_button.clicked.connect(self.delete_info)

    def put_add_info(self):
        pass

    def delete_info(self):
        pass

    def get_detail_window(self):        # 打开详细页面窗口
        self.detail_window = MaintainDetailWindow()
        self.detail_window.window.show()
    
    def get_modify_window(self):            # 打开修改页面窗口
        self.modify_window = MaintainModifyWindow()
        self.modify_window.window.show()
    
    def get_search_info(self):          # 获取搜索框信息
        self.search_info = self.window.search_info.text()
        print("搜索内容：",self.search_info)  

class MaintainDetailWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("MaintenanceDetail.ui")

class MaintainModifyWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("MaintenanceModify.ui")
        self.window.yes_button.clicked.connect(self.get_modify_info)
        self.window.concel_button.clicked.connect(lambda:self.window.close())

    def get_modify_info(self):          # 获取修改信息
        self.modify_name = self.window.name_line.text()
        self.modify_discribe = self.window.describe_line.text()
        self.modify_place = self.window.place_line.text()
        self.modify_time = self.window.time_line.text()
        self.modify_people = self.window.people_line.text()
        print("修改信息：", self.modify_name, self.modify_discribe,self.modify_place, self.modify_time, self.modify_people)
        self.window.close()

class DiseaseWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("DiseaseManagement.ui")
        self.window.detail_button.clicked.connect(self.get_detail_window)
        self.window.modify_button.clicked.connect(self.get_modify_window)
        self.window.search_button.clicked.connect(self.get_search_info)
        self.window.add_button.clicked.connect(self.put_add_info)
        self.window.delete_button.clicked.connect(self.delete_info)

    def put_add_info(self):
        pass

    def delete_info(self):
        pass

    def get_detail_window(self):
        self.detail_window = DiseaseDetailWindow()
        self.detail_window.window.show()
    
    def get_modify_window(self):
        self.modify_window = DiseaseModifyWindow()
        self.modify_window.window.show()

    def get_search_info(self):
        self.search_info = self.window.search_info.text()
        print("搜索内容：",self.search_info)  

class DiseaseDetailWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("DiseaseDetail.ui")

class DiseaseModifyWindow:
    def __init__(self) -> None:
        self.window = QUiLoader().load("DiseaseModify.ui")

class MainWindow:
    def __init__(self) :
        self.window = QUiLoader().load("主界面.ui")
        self.window.pushButton.clicked.connect(self.get_maintain_window)
        self.window.pushButton_2.clicked.connect(self.get_disease_window)

    def get_maintain_window(self):
        self.maintain_window = MaintainWindow()
        self.maintain_window.window.show()
        self.window.close()

    def get_disease_window(self):
        self.disease_window = DiseaseWindow()
        self.disease_window.window.show()
        self.window.close()


app = QApplication([])
dis = MainWindow()
dis.window.show()
app.exec_()