from flask import Blueprint, request, json, g
from dacite import from_dict
from dacite_config import config
from students import dataclasses, datahelper, errors
from results import make_data_result
from datetime import datetime

blueprint = Blueprint("students", import_name = "students")


#查詢所有資料
@blueprint.route('/get_students', methods=["GET"])
def get_students():
    #1. 取得產品
    s = datahelper.get_students()
   #2. 回傳產品
    return json.jsonify(make_data_result(s))



#新增資料 json傳入 username password
@blueprint.route('/create_student', methods=["POST"])
def create_student():
    #1. 解析JSON或參數
    x = json.loads(request.data)
    obj = from_dict(dataclasses.CreateStudent, x, config=config)
    #2. 驗證資料
    #3. 建立產品
    #3.1. 新增學生資料
    s = datahelper.create_student(obj.student_name, obj.student_number)
    # 學號存在return false
    if s == False:
        return json.jsonify(errors.e2001)

    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))



#修改資料 
@blueprint.route('/update_student', methods=["PUT"])
def update_student():
    #1. 解析JSON或參數
    #1.1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.UpdateStudent, x, config=config)

    #2. 驗證資料
    #2.1. 驗證student_number是否存在
    if  datahelper.is_student_name_existed(obj.student_name) == False:
        return json.jsonify(errors.e3001) 
    # 檢查?
    print(obj.new_student_name, obj.new_student_number, obj.student_name, '------------------')
    #3.1. 更新產品
    s = datahelper.update_student(obj.new_student_name, obj.new_student_number, obj.student_name)
    #3.2. 提交
    g.cursor().connection.commit()
   #4. 回傳產品
    return json.jsonify(make_data_result(s))



#刪除資料
@blueprint.route('/delete_student', methods=["DELETE"])
def delete_user():

    #1. 解析JSON
    x = json.loads(request.data)
    obj = from_dict(dataclasses.DeleteStudent, x, config=config)
    #2. 驗證資料
    #2.1. 驗證todo_id是否存在
    if  datahelper.is_student_name_existed(obj.student_name) == False:
        return json.jsonify(errors.e4001) 
    #3. 刪除資料
    #3.1. 刪除資料
    s = datahelper.delete_student(obj.student_name)
    #3.2. 提交
    g.cursor().connection.commit()
    #4. 回傳是否成功刪除
    return json.jsonify(make_data_result(s))



#-------------------------------------------------------------------------------------


