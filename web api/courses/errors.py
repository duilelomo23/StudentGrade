from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")

#給get get_course API使用的error
e1001 = make_error_result("1001","課名或老師不可空白")



#給post create_course API使用的error
e2001 = make_error_result("e2001","課名或老師不可空白")
e2002 = make_error_result("e2002","課名已重複")


#給update API使用的error
e3001 = make_error_result("e3001", "課名或老師不可空白")
e3002 = make_error_result("e3002","輸入課名不存在")

#給delete API使用的error
e4001 = make_error_result("e4001","course_name不存在")