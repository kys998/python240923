# DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯 메소드
    def firstClick(self):

        url = "http://www.daangn.com/fleamarket"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        # 검색이 용이한 객체로 만들기
        soup = BeautifulSoup(response.text, "html.parser")

        # 상단의 <div> 태그를 모두 검색
        # 파일로 저장
        f = open("daangn.txt", "a+", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            regionElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            region = regionElem.text.strip()

            #f-string 포매팅
            print(f"{title}, {price}, {region}")
            f.write(f"{title}, {price}, {region}\n")
        f.close()            
        self.label.setText("당근마켓 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭했음")  

# 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
