#DATABASE CONNECTIVITY


import pymysql

#Que-1.

print('''Create a database. Create the following tables:\n
1. Book\n
2. Titles\n
3. Publishers\n
4. Zipcodes\n
5. AuthorsTitles\n
6. Authors\n
Refer to the diagram below\n''')


db=pymysql.connect("localhost",'root','yogesh@123456','demo')
cursor=db.cursor()
cursor.execute("create table book(book_id int,title_id int,location varchar(20),genre char(20))")
cursor.execute(" create table titles(title_id int,title char(20),isbn int,publisher_id varchar(20),publication_year int)")
cursor.execute("create table Authors_Titles(Author_Title_id varchar(20),Author_id varchar(20),Title_id varchar(20))")
cursor.execute("create table Publishers(Publisher_id varchar(20),Name char(20),Street_Address varchar(30),Sute_Number int,Zip_Code_id varchar(20))")
cursor.execute("create table Authors(Author_id varchar(20),First_Name char(20),Middle_Name char(20),Last_Time char(20))")
cursor.execute("create table Zip_Codes(Zip_Code_id varchar(20),City char(20),State char(20),Zip_Code varchar(20))")
db.close()

print("\n*********************************\n")


#Que-2.

print("Insert values in the tables.\n")


db1=pymysql.connect("localhost",'root','yogesh@123456','demo')
cursor=db1.cursor()
cursor.execute("insert into book values(111,222,'delhi','mybook')")
cursor.execute("insert into titles values(001,'Its_me',202,'pub12',2018)")
cursor.execute("insert into Authors_Titles values('aa22','abc1','zxy9')")
cursor.execute("insert into Publishers values('me23','yogesh','NewDelhi12',232,'zip1212')")
cursor.execute("insert into Authors values('Auth12','yogesh','yogi','prajapat')")
cursor.execute("insert into Zip_Codes values('Zip11','Mumbai','Maharashtra','Zipcode99')")
db1.commit()
db1.close()

print("\n*********************************\n")


#Que-3.

print(" Update any values in any of the tables. Print the original and updated values.\n")


db2=pymysql.connect("localhost",'root','yogesh@123456','demo')
cursor=db2.cursor()
cursor.execute("select * from book")
cursor.execute("update book set location='Mumbai' where location='delhi'")
db2.commit()
cursor.execute("select * from book")
db2.close()
