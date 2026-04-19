import sys
import random
from PyQt6.QtWidgets import(QApplication, QWidget, QLabel, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt

menu = ["ผัดกะเพรา", "ข้าวผัด", "ผัดพริกแกง", "คะน้า", "แขนง", "สุกกี้น้ำ", "สุกี้แห้ง", "ผัดขี้เมา"]
proteins = ["หมู", "เนื้อ", "ไก่", "หมูกรอบ", "ทะเล"]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("วันนี้กินอะไรดี")
        self.setGeometry(350,150,500,500)
        self.mainDesign()
        self.UI()

    def mainDesign(self):
        self.setStyleSheet("""
            QWidget{
                background-color: #FFF7E6;
                font-size: 14pt;
                font-family: Arial;
                color: #5C3D2E;
            }
            QLabel {
                color: #5C3D2E;
            }
            QPushButton{
                background-color: #FF9F43;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                border: none;
            }
            QPushButton:hover {
                background-color: #FF81C1A;              
            }
            QPushButton:pressed {
                background-color: #E67000;              
            }
            QLineEdit, QTextEdit {
                background-color: #FFFFFF;
                border: 1px solid #F1C5A1;
                border-radius: 5px;
                padding: 5px 8px;
            }
            QListWidget {
                border: 1px solid #F1C5A1;
                border-radius: 5px;
                background-color: #FFFDF8;
            }
        """)
    
    def UI(self):
        mainLayout = QVBoxLayout()
        mainLayout.addStretch()

        self.greeting = QLabel()
        self.greeting.setTextFormat(Qt.TextFormat.RichText)
        self.greeting.setText("""
            <div style="text-align:center;">
            <span style="font-size:18pt; font-weight:normal;">
                ยินดีต้อนรับสู่โปรแกรมสุ่มอาหาร
            </span>
            <br>
            <span style="font-size:20pt;font-weight:normal;">
                กด 
            </span>
            <span style="font-size:22pt;font-weight:bold;">
                “สุ่มเลย”
            </span>
            <span style="font-size:20pt;font-weight:normal;">
                ได้เลย!
            </span>
            </div>
            """)
        
        self.greeting.setWordWrap(True)
        self.greeting.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        mainLayout.addWidget(self.greeting)
        mainLayout.addSpacing(20)

        btnRandom = QPushButton('สุ่มเลย')
        btnExit = QPushButton("ปิดโปรแกรม")

        btnRandom.clicked.connect(self.RandomClicked)
        btnExit.clicked.connect(self.close)

        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        btnLayout.addWidget(btnRandom)
        btnLayout.addStretch()       
        btnLayout.addWidget(btnExit)
        btnLayout.addStretch()
        btnLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainLayout.addLayout(btnLayout)
        mainLayout.addStretch()
    
        self.setLayout(mainLayout)

    def menu_pool(self):
        #pool = [(m,p)for m in menu for p in proteins]
        pool = []
        for m in menu:
            for p in proteins:
                pool.append((m,p))
        return (pool)
    
    def RandomClicked(self):
        pool = self.menu_pool()
        while True:
            if not pool:
                QMessageBox.information(self,"สุ่มจดหมด","สุ่มจนหมดยังเลือกไม่ได้อีกหรอ~")
                return
            
            outputMenu, outputProtein = pool.pop()

            box = QMessageBox(self)
            box.setWindowTitle("วันนี้กินอะไรดี")
            box.setTextFormat(Qt.TextFormat.RichText)
            box.setText(f"""
                <div style="text-align:center;">
                <span style="font-size:16pt; font-weight:normal;">ผลการสุ่ม</span>
                <br>
                <span style="font-size:18pt; font-weight:normal">เมนูวันนี้คือ</span>
                <br>
                <span style="font-size:22pt; font-weight:bold;">{outputMenu}{outputProtein}</span>
                </div>
                """)


            btnOK = box.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
            btnReroll = box.addButton("สุ่มใหม่", QMessageBox.ButtonRole.ActionRole)
            box.setDefaultButton(btnOK)
            box.exec()
            
            if box.clickedButton() is btnOK:
                return
            else:
                continue

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()