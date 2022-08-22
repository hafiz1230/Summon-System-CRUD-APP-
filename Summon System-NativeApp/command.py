import sys
import sqlite3
from traceback import print_tb

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from os import path

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

from windows.confirm_update import Ui_confirm_window
from windows.confirm_delete import Ui_delete_window
from windows.confirm_add import Ui_add_window

from werkzeug.security import generate_password_hash, check_password_hash

# current_iteration=0




class WelcomeScreen(QMainWindow): 
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        uic.loadUi('windows\login_screen_window.ui',self)
        self.login_btn.clicked.connect(self.gotomain)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def gotomain(self):
        user=self.username.text()
        password=self.password.text()
        
        
        db=self.connectDB()
        cursor=db.cursor()

        command = ('''
                    SELECT password FROM user WHERE email=?
                    ''' )

        target = cursor.execute(command,(user,))

        db.commit()

        pass_in_table=None
        hadir=str()
        for row in target: #Target contain password from inputted email
            hadir=row[0]   #Hadir is sha256 password
            
        
        if len(user)==0  :
                self.error.setText("Please input all field")

        elif len(hadir) >0:
            print('User existed')
            

            if check_password_hash(hadir,password)==True:
                main_window= MainWindow()
                widget.addWidget(main_window)
                widget.setCurrentIndex(widget.currentIndex()+1)
                self.password.setText("")
                print('login passed')
            else :
                self.error.setText("Invalid username or password")  
                print('login not passed') 

        elif len(hadir)==0:
            print('User not existed')
            self.error.setText("User not existed") 
        
        else:
            self.error.setText("Error") 
        
        print('\n')


    def connectDB(self):
        #return sqlite3.connect('db.sqlite')
        return sqlite3.connect(r"C:\Users\hafiz\Desktop\KIX3004-Asgn-G3-WebApp\RSS\project\db.sqlite")  
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('main.ui', self)
        self.current_iteration=int()
        self.search_count = int()
        

        self.GET_DATA()
        self.Handel_buttons()
        
        
    def connectDB(self):
        #return sqlite3.connect("mydb.db")
        return sqlite3.connect(r"C:\Users\hafiz\Desktop\KIX3004-Asgn-G3-WebApp\RSS\mydb.db") 

    def prev_next_button(self):
                
        if self.current_iteration<=0 :
            self.next_btn.setEnabled(True)
            self.previous_btn.setDisabled(True)
        if self.current_iteration>0 and self.current_iteration< self.search_count-1  :
            self.next_btn.setEnabled(True)
            self.previous_btn.setEnabled(True)
        if self.current_iteration>=self.search_count-1  : 
            self.next_btn.setDisabled(True)
            self.previous_btn.setEnabled(True)

    def Handel_buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.add_btn.clicked.connect(self.ADD_DATA_WINDOW)

        self.search_btn_edit.clicked.connect(self.SEARCH_ID)
        
        self.next_btn.clicked.connect(self.NEXT_SEARCH)
        self.previous_btn.clicked.connect(self.PREV_SEARCH)

        self.clear_btn.clicked.connect(self.CLEAR)
        self.delete_btn.clicked.connect(self.DELETE_WINDOW)
        self.update_btn.clicked.connect(self.UPDATE_WINDOW)
        self.logout_btn.clicked.connect(self.LOG_OUT)
        self.search_page1.clicked.connect(self.SEARCH_PLATE_PAGE1)

    def SEARCH_PLATE_PAGE1(self):
        db=self.connectDB()
        cursor=db.cursor()

        target_no= self.no_plate_page1.text().upper()
        command='''SELECT * FROM datas WHERE no_plate=?'''
        result = cursor.execute(command,(target_no,))
        db.commit()

        if len(target_no) != 0:
            self.table.setRowCount(0)

            for row_number , row_data in enumerate(result):
                self.table.insertRow(row_number)
                for column_number ,data in enumerate(row_data):
                    self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))   

    def LOG_OUT(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    
    def UPDATE(self,dialog_button):
        
        # if self.ui_update.button_update.accepted :
        #     print("OK!")

        value=dialog_button.text() 
        
        if value == 'OK' :

            db=self.connectDB()
            cursor=db.cursor()

            no_plate= self.search_plate.text().upper()
            issue_date=self.issue_date_box.text()
            location=self.location_box.text()
            offense=self.offense_box.text()
            status=self.status_box.text()
            reported=self.reported_box.text()
            
            target_no=self.search_plate.text().upper()
            target=cursor.execute(''' SELECT * from datas WHERE no_plate=?''',(target_no,))
            search_table=target.fetchall()
            db.commit()

            # print(search_table[self.current_iteration][6])
            date_searched=search_table[self.current_iteration][6]
            
            command = ''' UPDATE datas
                    SET issue_date = ? ,
                        location = ? ,
                        offence = ? ,
                        status = ? ,
                        reported_by = ?
                    WHERE no_plate = ? AND date = ?'''
            
            cursor.execute(command,(issue_date,location,offense,status,reported,no_plate,date_searched))
            db.commit()
            self.window_update.close()


        elif value=='Cancel' :
            self.window_update.close()
    
    def UPDATE_WINDOW(self):
        
        self.window_update = QtWidgets.QDialog()
        self.ui_update = Ui_confirm_window()
        self.ui_update.setupUi(self.window_update)
        self.window_update.show()
        
        self.ui_update.button_update.clicked.connect(self.UPDATE)

    def GET_SEARCH_TABLE(self):
        db=self.connectDB()
        cursor=db.cursor()
        target_no=self.search_plate.text().upper()
        target=cursor.execute(''' SELECT * from datas WHERE no_plate=?''',(target_no,))
        search_table=target.fetchall()
        db.commit()
        
        return search_table


    def DELETE(self,dialog_button):
        
        value=dialog_button.text() 

        search_table=self.GET_SEARCH_TABLE()
        date_searched=search_table[self.current_iteration][6]

        if value == 'OK' :
            db=self.connectDB()
            cursor=db.cursor()
            
            target_no=self.search_plate.text().upper()
            
            #command='''DELETE FROM datas WHERE no_plate = ? , issue_date = ?'''
            cursor.execute('DELETE FROM datas WHERE date = ? AND no_plate=? ',(date_searched,target_no))
            db.commit() 

            self.search_plate.setEnabled(False)
            self.issue_date_box.setEnabled(False)
            self.location_box.setEnabled(False)
            self.offense_box.setEnabled(False)
            self.status_box.setEnabled(False)
            self.reported_box.setEnabled(False)

            
            self.current_iteration=0

            self.window_delete.close()
        
        elif value=='Cancel':
            self.window_delete.close()    

    def DELETE_WINDOW(self):
        self.window_delete=QtWidgets.QDialog()
        self.ui_delete=Ui_delete_window()
        self.ui_delete.setupUi(self.window_delete)   
        self.window_delete.show()

        self.ui_delete.button_delete.clicked.connect(self.DELETE)
        
    def CLEAR(self):
        self.issue_date_box.setText("")
        self.location_box.setText("")
        self.offense_box.setText("")
        self.status_box.setText("")
        self.reported_box.setText("")
        self.search_plate.setText("")

        self.next_btn.setEnabled(True)
        self.previous_btn.setEnabled(True)
    
    def GET_DATA(self):
    
        db=self.connectDB()
        cursor=db.cursor()
        
        command= ''' SELECT * from datas '''
        
        result= cursor.execute(command)
        
        self.table.setRowCount(0)

        for row_number , row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number ,data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def ADD_DATA(self,dialog_button):
        db=self.connectDB()
        cursor=db.cursor()

        value= dialog_button.text()

        if value == 'OK' :
            no_plate= self.search_plate.text().upper()
            issue_date=self.issue_date_box.text()
            location=self.location_box.text()
            offense=self.offense_box.text()
            status=self.status_box.text()
            reported=self.reported_box.text()

            cursor.execute('''INSERT INTO datas (no_plate,issue_date,location,offence,status,reported_by) 
                    VALUES (?,?,?,?,?,?)''',(no_plate,issue_date,location,offense,status,reported));
            db.commit()
            print("Record created successfully")
            db.close()   
            self.window_add.close()  

        elif value =='Cancel' :
            self.window_add.close()      

    def ADD_DATA_WINDOW(self):
        self.window_add=QtWidgets.QDialog()
        self.ui_add=Ui_add_window()
        self.ui_add.setupUi(self.window_add)
        self.window_add.show()

        self.ui_add.button_add.clicked.connect(self.ADD_DATA)
        
    def SEARCH_ID(self):
        self.search_plate.setEnabled(True)
        self.issue_date_box.setEnabled(True)
        self.location_box.setEnabled(True)
        self.offense_box.setEnabled(True)
        self.status_box.setEnabled(True)
        self.reported_box.setEnabled(True)
        
        
        db=self.connectDB()
        cursor=db.cursor()
        
        target_no=self.search_plate.text().upper()
        target=cursor.execute(''' SELECT * from datas WHERE no_plate=?''',(target_no,))
        search_table=target.fetchall()
        db.commit()

        # global current_iteration
        print(self.current_iteration,"for current_iteration")   

        
        self.issue_date_box.setText(search_table[0][0])
        self.location_box.setText(search_table[0][2])  
        self.offense_box.setText(search_table[0][3]) 
        self.status_box.setText(search_table[0][4])
        self.reported_box.setText(search_table[0][5])

        

        for row in range(len(search_table)):
            self.search_count=self.search_count+1

        print("Max search count is ",self.search_count)         
        self.prev_next_button()
        # print(self.current_iteration)

    def SEARCH_NEXT_PREV(self):

        db=self.connectDB()
        cursor=db.cursor()
        target_no=self.search_plate.text().upper()
        target=cursor.execute(''' SELECT * from datas WHERE no_plate=?''',(target_no,))
        search_table=target.fetchall()
        db.commit()

        no=self.current_iteration
        self.issue_date_box.setText(search_table[no][0])
        self.location_box.setText(search_table[no][2])  
        self.offense_box.setText(search_table[no][3]) 
        self.status_box.setText(search_table[no][4])
        self.reported_box.setText(search_table[no][5])

        self.prev_next_button()



    def NEXT_SEARCH(self):
        print('next is clicked ')
        # global current_iteration
        self.current_iteration=self.current_iteration+1

        print(self.current_iteration,"for current_iteration (next search)")
        self.SEARCH_NEXT_PREV()

    def PREV_SEARCH(self):
        print('prev is clicked ')
        # global current_iteration
        self.current_iteration=self.current_iteration-1
        print(self.current_iteration,"for current_iteration(prev search)")
        self.SEARCH_NEXT_PREV()
        

if __name__ == '__main__':
    app= QApplication(sys.argv)
    # mainwindow=MainWindow()
    # mainwindow.show()
    
    widget = QtWidgets.QStackedWidget()
    firstwindow=WelcomeScreen()
    widget.addWidget(firstwindow)


    # #Test only
    # testwindow=TestScreen()
    # widget.addWidget(testwindow)

    # widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    widget.setFixedHeight(650)
    widget.setFixedWidth(840)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')