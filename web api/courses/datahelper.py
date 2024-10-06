from flask import g

# def add_customer(c):
#     db.append(c)

#get 查詢所有
def get_courses():
    cur = g.cursor()
    cur.execute(
        '''
        select * from course
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts



#post 新增
def create_course(course_name, teacher):
    cur = g.cursor()
    cur.execute(
        '''
        select * from course where course_name = %s
        ''',
        (course_name)
    )
    course_title = cur.fetchone()
    if course_title != None:
        return False


    cur.execute(
        '''
        insert into course
        (course_name, teacher)
        values
        (%s, %s)  
        ''',
        (course_name, teacher)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select * from course where course_id = %s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#判斷 course_name 是否存在 不存在return false
def is_course_name_existed(course_name):
    cur = g.cursor()
    cur.execute(
        '''
        select * from course where course_name=%s
        ''',
        (course_name)
    )
    ret_dict = cur.fetchone()

    return ret_dict != None
#修改
def update_course(old_course_name, new_course_name, new_teacher):
    cur = g.cursor()

    cur.execute(
        '''
        update course
        set course_name=%s, teacher=%s
        where course_name=%s 
        ''',
        (new_course_name, new_teacher, old_course_name)
    )


    cur.execute(
        '''
        select * from course where course_name=%s and teacher=%s
        ''',
        (new_course_name, new_teacher)
    )
    ret_dict = cur.fetchone()

    return ret_dict

#刪除
def delete_course(course_name):

    cur = g.cursor()
    cur.execute(
            '''
            delete from course where course_name = %s
            ''',
            (course_name)
        )
 
    rowcount = cur.rowcount
    
    return rowcount > 0

#-----------------------------------------------------------------------------

