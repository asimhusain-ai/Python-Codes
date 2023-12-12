import sqlite3
cno=sqlite3.connect('bt3a.db')
cno.execute('''create table employee(
    code varchar not null,
    name varchar not null,
    salary number null
);''')
print("Table Created")
cno.execute("insert into employee(code,name,salary) values('S2102','Micheal',23001)")
cno.execute("insert into employee(code,name,salary) values('S2103','John',23002)")
print("Data Inserted")
cno.commit()
'''cno.execute("delete from employee WHERE code = 'S2103'")'''
cno.execute("update employee set salary = '234000' where code = 'S2102'")
crs=cno.execute("select * from employee")
for rs in crs:
    print("Employee Id:",rs[0])
    print("Employee Name:",rs[1])
    print("Employee Salary:",rs[2])