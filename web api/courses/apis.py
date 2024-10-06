from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from courses import dataclasses, datahelper, errors
from results import make_data_result
from datetime import datetime

blueprint = Blueprint("course", import_name = "course")


#查詢所有資料
@blueprint.route('/get_courses', methods=["GET"])
def get_courses():
    #1. 解析JSON或參數
    #2. 驗證資料
    #3. 取得產品
    s = datahelper.get_courses()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))



#新增
@blueprint.route('/create_course', methods=["POST"])
def create_course():  
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.CreateCourse, x, config=config)
    #2. 驗證資料
    #2.1. title不可為空白
    if len(obj.course_name) == 0  or len(obj.teacher) == 0:
        return json.jsonify(errors.e2001)
    #3. 建立產品
    #3.1. 建立產品
    s = datahelper.create_course(obj.course_name, obj.teacher)
    if s == False:
        return json.jsonify(errors.e2002)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#修改
@blueprint.route('/update_course', methods=["PUT"])
def update_course():
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateCourse, x, config=config)
    #2. 驗證資料
    #2.1 判斷是否為空
    if not obj.course_name.strip() or not obj.new_course_name.strip() or not obj.new_teacher.strip():
        return json.jsonify(errors.e3001)
    #3. 更新產品
    #3.1. 更新產品
    s = datahelper.update_course(obj.course_name, obj.new_course_name, obj.new_teacher)
    if s == False:
        return json.jsonify(errors.e3002)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#刪除
@blueprint.route('/delete_course', methods=["DELETE"])
def delete_course():
    x = json.loads(request.data)
    obj = from_dict(dataclasses.DeleteCourse, x, config=config)
    

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(obj.course_name, str) == False or \
          datahelper.is_course_name_existed(obj.course_name) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    success = datahelper.delete_course(obj.course_name)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))



#------------------------------------------------------------------------------------------------------
#student_course api

#查詢單筆資料   
@blueprint.route('/get_course/<course_id>', methods=["GET"])
def get_course(course_id):
    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        course_id = int(course_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(course_id, int) == False or \
          datahelper.is_course_id_existed(course_id) == False:
        return json.jsonify(errors.e2001)
    #3. 取得產品
    s = datahelper.get_course(course_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))



#搜索 student_id 是否擁有 course_id
@blueprint.route('/get_student_exists_course/<student_id>/<course_id>', methods=["GET"])
def get_student_exists_course(student_id, course_id):

    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        course_id = int(course_id)
        student_id = int(student_id)
        print(course_id, student_id,'*------------------------------')
    except:
        pass
        
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(course_id, int) == False or \
        isinstance(student_id, int) == False:
        return json.jsonify(errors.e2002)
    if datahelper.serch_course_and_student_id_update_existed(student_id) == 0:
        return json.jsonify(errors.e2002)

    #3. 取得產品
    s = datahelper.serch_student_course_date(student_id ,course_id)
   #4. 回傳產品

    return json.jsonify(make_data_result(s))


#搜索student_id 購買所有紀錄
@blueprint.route('/get_student_all_course_record/<student_id>', methods=["GET"])
def get_student_all_course_record(student_id):

    #1. 解析JSON或參數
    #1.1. 解析todo_id為int
    try:
        student_id = int(student_id)
    except:
        pass

    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  isinstance(student_id, int) == False or \
        datahelper.serch_course_and_student_id_update_existed(student_id) == False:
        return json.jsonify(errors.e2002)
    #3. 取得產品
    s = datahelper.serch_student_all_course(student_id)
   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#新增購買紀錄  
@blueprint.route('/create_update_course_record/<student_id>/<course_id>', methods=["POST"])
def create_update_course_record(student_id, course_id):
    #1. 解析JSON或參數
    # x = json.loads(request.data)
    # obj = from_dict(dataclasses.Createstudent, x, config=config)
    #2. 驗證資料
    #1.1. 解析todo_id為int
    try:
        student_id = int(student_id)
        course_id = int(course_id)
    except:
        pass
    #3. 建立產品
    #3.1. 建立產品
    s = datahelper.create_update_course_record(student_id, course_id, datetime.now())


    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

