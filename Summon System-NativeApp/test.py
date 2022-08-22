

import sqlite3




user='1'
password=1

db=sqlite3.connect('mydb.db')  
cursor=db.cursor()

# command = ('''
#         SELECT password FROM user WHERE email=?
#         ''' )

# target = cursor.execute(command,(user,))

# db.commit()

target_no='WKE123'
target=cursor.execute(''' SELECT * from datas WHERE no_plate=?''',(target_no,))
asd=target.fetchall()
db.commit()

row=0
col=0

print(len(asd))

search=int()
for row in range(len(asd)):
    search=search+1
    for col in range(len(asd[row])):
        if col==0:
            self.issue_date_box.setText(asd[row][col])
        if col==2:
            self.location_box.setText(asd[row][col])    
        if col==3:
            self.offense_box.setText(asd[row][col])
        if col==4:
            self.status_box.setText(asd[row][col])
        if col==5:
            self.reported_box.setText(asd[row][col])
print("Max search count is ",search_count)
# print(search)


# [('29/12/2020', 'WKE123', 'MBasdasd', 'Trafik', 'Pending', 'Muaz', '2022-01-02 17:21:51'), 
# ('29/12/2020', 'WKE123', 'MBasdasd', 'Trafik', 'Pending', 'Muaz', '2022-01-02 17:24:40'), 
# ('asd', 'WKE123', 's', 'asd', 'asd', 'ss', '2022-01-27 08:34:41')]
search_count=int()
for row in search_table:
        search_count=search_count+1
        if row==0 :
            for col in row:
                if col==0:
                    self.issue_date_box.setText(data)
                if col==2:
                    self.location_box.setText(data)    
                if col==3:
                    self.offense_box.setText(data)
                if col==4:
                    self.status_box.setText(data)
                if col==5:
                    self.reported_box.setText(data)
print("Max search count is ",search_count) 