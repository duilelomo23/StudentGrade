from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給get_grade API使用的error
e1001 = make_error_result("e1001","title不可為空白")

#給create_grade API使用的error
e2001 = make_error_result("e2001","學生名稱或課程名稱不存在")
e2002 = make_error_result("e2002", "'請輸入0-100'")
e2003 = make_error_result("e2003", "該學生課程已存在成績")


#給update API使用的error
e3001 = make_error_result("e3001","學生名稱或課程名稱不存在")


#給delete API使用的error
e4001 = make_error_result("e4001","todo_id不存在")