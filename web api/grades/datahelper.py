from flask import g

# def add_customer(c):
#     db.append(c)




#get搜索所有資料
def get_grades():
    cur = g.cursor()
    cur.execute(
        '''
        select student.student_name, student.student_number, course.course_name, course.teacher, student_grade.grade
        from student_grade
        inner join student on student.student_id = student_grade.student_id 
        inner join course on course.course_id = student_grade.course_id 
        
        '''
    )
    ret_dicts = cur.fetchall()

    return ret_dicts


#create_grade 學生是否存在並獲取學生id 
def get_student_id(student_name):
    cur = g.cursor()
    cur.execute(
        '''
        select student_id from student where student_name=%s
        ''',
        (student_name)
    )
    ret_dicts = cur.fetchone()
    if ret_dicts is None:
        return False
    return ret_dicts['student_id']


#create_grade 課程是否存在並獲取學生id 
def get_course_id(course_name):
    cur = g.cursor()
    cur.execute(
        '''
        select course_id from course where course_name=%s
        ''',
        (course_name)
    )
    
    ret_dicts = cur.fetchone()
    if ret_dicts is None:
        return False
    return ret_dicts['course_id']


#create_grade 是否已輸入成績
def is_student_grade_exist(student_id, course_id):
    cur = g.cursor()
    cur.execute(
        '''
        select * from student_grade where student_id=%s and course_id=%s
        ''',
        (student_id, course_id)
    )
    
    ret_dicts = cur.fetchone()
    
    return ret_dicts == None

#新增
def create_grade(student_id, course_id, grade):
    cur = g.cursor()
    
    cur.execute(
    
        '''
        insert into student_grade
        (student_id , course_id, grade)
        values
        (%s, %s, %s)  
        ''',
        (student_id, course_id, grade)
    )
    new_id = cur.lastrowid
    cur.execute(
        '''
        select student.student_name, student.student_number, course.course_name, course.teacher, student_grade.grade
        from student_grade 
        inner join student on student.student_id = student_grade.student_id 
        inner join course on course.course_id = student_grade.course_id 
        where student_grade_id=%s
        ''',
        (new_id)
    )
    ret_dict = cur.fetchone()

    return ret_dict


#更新grade title description
def update_grade(student_id, course_id, grade):
    cur = g.cursor()
    cur.execute(
        '''
        update student_grade
        set grade=%s 
        where student_id=%s and course_id=%s
        ''',
        (grade, student_id, course_id)
    )

    cur.execute(
        '''
        select student.student_name, student_number, course.course_name, course.teacher, student_grade.grade
        from student_grade
        inner join student on student.student_id = student_grade.student_id 
        inner join course on course.course_id = student_grade.course_id 
        where student_grade.student_id=%s and student_grade.course_id=%s
        ''',
        (student_id, course_id)
    )
    ret_dict = cur.fetchone()
    return ret_dict


#grade_id刪除資料
def delete_grade(student_id, course_id):
    cur = g.cursor()
    cur.execute(
            '''
            delete from student_grade where student_id=%s and course_id=%s
            ''',
            (student_id, course_id)
        )
    rowcount = cur.rowcount
    return rowcount > 0



#-------------------------------------------------

