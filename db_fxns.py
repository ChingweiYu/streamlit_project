import sqlite3
conn = sqlite3.connect('data1.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS taskstable(School_number_text TEXT,PersonName TEXT,Gender TEXT,Birth_date TEXT,College TEXT,Grades TEXT)')



def add_data(School_number_text,PersonName,Gender,Birth_date,College,Grades):
	c.execute('INSERT INTO taskstable(School_number_text,PersonName,Gender,Birth_date,College,Grades) VALUES (?,?,?,?,?,?)',(School_number_text,PersonName,Gender,Birth_date,College,Grades))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM taskstable')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT School_number_text FROM taskstable')
	data = c.fetchall()
	return data

# def get_task(task):
# 	c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
# 	data = c.fetchall()
# 	return data

# def get_task_by_status(task_status):
# 	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
# 	data = c.fetchall()


def edit_task_data(School_number_text,PersonName,Gender,Birth_date,College,Grades):
    # sql = 'UPDATE taskstable SET PersonName='+PersonName+',Gender='+Gender',Birth_date='+Birth_date+',College='+College+',Grades='+Grades+'WHERE School_number_text='+School_number_text+';'
    	
    
	c.execute('UPDATE taskstable SET PersonName=?,Gender=?,Birth_date=?,College=?,Grades=? WHERE School_number_text=? ;',(PersonName,Gender,Birth_date,College,Grades,School_number_text))
	conn.commit()
	# data = c.fetchall()
	# return data

def delete_data(School_number_text):
	
	# c.execute('DELETE FROM taskstable WHERE School_number_text=?',(School_number_text))
	sql = 'DELETE FROM taskstable WHERE School_number_text='+str(School_number_text)
	c.execute(sql)
	conn.commit()
