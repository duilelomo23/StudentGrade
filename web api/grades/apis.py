from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from grades import dataclasses, datahelper, errors
from results import make_data_result

blueprint = Blueprint("grades", import_name = "grades")


#獲取所有grade
@blueprint.route('/get_grades', methods=["GET"])
def get_grades():
    #1. 解析JSON或參數
    #2. 驗證資料
    #3. 取得產品
    s = datahelper.get_grades()

   #4. 回傳產品
    return json.jsonify(make_data_result(s))


#新增grade  傳入 json 學生名稱 student_name 課程名稱 course_name  課程成績 grade
@blueprint.route('/create_grade', methods=["POST"])
def create_grade():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.Creategrade, x, config=config)
    #2. 驗證資料 成績是否為整數
    try:
        grade = int(obj.grade)
    except:
        return json.jsonify(errors.e2002)
    #2.1 成績最高100
    if grade > 100:
        return json.jsonify(errors.e2001)
    #2.2. 判斷學生是否存在 return 學生id
    student_id = datahelper.get_student_id(obj.student_name)
    #2.3判斷課程是否存在 return 課程id
    course_id = datahelper.get_course_id(obj.course_name)
    if student_id == False or course_id == False:
        return json.jsonify(errors.e2001)
    #成績存在回傳false
    bool_is_student_grade_exist = datahelper.is_student_grade_exist(student_id, course_id)
    if bool_is_student_grade_exist == False:
        return json.jsonify(errors.e2003)
    #3. 建立產品
    #3.1. 建立產品
    s = datahelper.create_grade(student_id, course_id, grade)        
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#更新grade
@blueprint.route('/update_grade', methods=["PUT"])
def update_grade():
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.Updategrade, x, config=config)
    #1.2. 解析grade_id為int
    try:
        grade = int(obj.grade)
    except:
        pass
    if grade > 100:
        return json.jsonify('請輸入0-100')

    #2. 驗證資料
    #2.1. 驗證grade_id是否存在
    student_id = datahelper.get_student_id(obj.student_name)
    #2.3判斷課程是否存在 return 課程id 不存在 return false
    course_id = datahelper.get_course_id(obj.course_name)
    if student_id == False or course_id == False:
        return json.jsonify(errors.e3001)
        #3. 更新產品
    #3.1. 更新產品
    s = datahelper.update_grade(student_id, course_id, grade)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))

#刪除grade
@blueprint.route('/delete_grade', methods=["DELETE"])
def delete_grade():

    #1. 解析JSON
    #1.1. 解析grade_id為int
    x = json.loads(request.data)
    obj = from_dict(dataclasses.Deletegrade, x, config=config)

    #2. 驗證資料
    #2.1. 驗證grade_id是否存在
    student_id = datahelper.get_student_id(obj.student_name)
    course_id = datahelper.get_course_id(obj.course_name)
    if student_id == False or course_id == False:
        return json.jsonify('學生名稱或課程不存在')
    #3.1. 刪除資料
    success = datahelper.delete_grade(student_id, course_id)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result({"success":success}))




#------------------------------------------------------------

