from flask import g

# def add_customer(c):
#     db.append(c)






#查詢所有資料
def get_students():
    cur = g.cursor()
    cur.execute(
        '''
        select * from student
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts


#新增資料
def create_student(student_name, student_number):
    cur = g.cursor()
    cur.execute(
        '''
        select * from student where student_number = %s
        ''',
        (student_number)
    )
    select_username = cur.fetchone()
    if select_username != None:
        return False

    cur.execute(
        '''
        insert into student
        (student_name, student_number)
        values
        (%s, %s)  
        ''',
        (student_name, student_number)
    )

    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from student where student_id = %s
        ''',
        (new_id)
    )

    ret_dict = cur.fetchone()

    return ret_dict





# put 判斷studet.number是否存在
def is_student_name_existed(student_name):
    cur = g.cursor()
    cur.execute(
        '''
        select * from student where student_name=%s
        ''',
        (student_name)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None




#修改學生資料
def update_student(new_name, new_number, old_name):
    cur = g.cursor()
    cur.execute(
        
        '''
        update student
        set student_name=%s, student_number=%s
        where student_name=%s 
        ''',
        (new_name, new_number, old_name)
    )
    cur.execute(
        '''
        select * from student where student_name=%s
        ''',
        (new_name)
    )
    ret_dict = cur.fetchone()

    return ret_dict




#刪除user_id資料
def delete_student(student_name):

    cur = g.cursor()
    cur.execute(
            '''
            delete from student where student_name = %s
            ''',
            (student_name)
        )
    rowcount = cur.rowcount
    return rowcount > 0















