from selenium.webdriver.common.by import By

"""登录页面配置数据"""
#  我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号，去登录
login_account_link = By.ID, "com.yunmall.lc:id/textView1"
# 账号
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID,"com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID,"com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID,  "com.yunmall.lc:id/tv_user_nikename"
# 设置按钮
login_set_btn  = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
#  消息推送
login_set_notification = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_set_modify_pwd = By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 退出按钮
login_set_logout_btn = By.ID, "com.yunmall.lc:id/setting_logout"
# 确定退出
login_set_right_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

"""以下为地址管理配置数据"""
# 设置—地址管理
set_address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人框
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 手机号框
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 选择地区
address_capital = By.ID, "com.yunmall.lc:id/address_province"
# 详细地址框
address_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编框
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_btn_send = By.ID, "com.yunmall.lc:id/button_send"
# 收件人列表
receipt_name_list = By.ID, "com.yunmall.lc:id/receipt_name"
# 地址管理—地址
address_info = By.ID, "com.yunmall.lc:id/receipt_address"
# 编辑按钮
address_compile = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改按钮
address_alter = By.ID, "com.yunmall.lc:id/modify"
# 删除
address_delete = By.ID, "com.yunmall.lc:id/delete"
# 确认删除
address_delete_ok = By.ID, "com.yunmall.lc:id/ymdialog_left_button"