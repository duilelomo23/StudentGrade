from results import make_error_result

# #給unregister API使用的error
# e2001 = make_error_result("e2001","此客戶名字不存在")



#給get_todo API使用的error
e1001 = make_error_result("e1001","user_id不存在")


#給create_product API使用的error
e2001 = make_error_result("e2001","學號已存在請更換學號")


#給update API使用的error
e3001 = make_error_result("e3001","學生學號不存在")


#給delete API使用的error
e4001 = make_error_result("e4001","學生學號不存在")

