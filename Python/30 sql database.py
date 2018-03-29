import sqlite3
cop= sqlite3.connect("myd.db")

# cop.execute("create table student (rollno int not null, name text not null, age int not null)")

# val= (12,'Sridhar',29),(10,'Michelle',46),(22,'Mohan',31)
# cop.executemany("insert into student (rollno, name, age) values (?,?,?)",val)

# cop.execute("update student set rollno=18 where age=29")

# cop.execute("delete from student where name='Sridevi'")

# cop.execute("drop table student")

# cop.commit()
for n in cop.execute("select rollno, name, age from student"):
    print("rollno: ",n[0], "name: ",n[1], "age: ",n[2])
