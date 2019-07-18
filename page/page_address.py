import page
from base.base import Base


class PageAddress(Base):
    # 点击 新增地址
    def page_click_address_add_new_btn(self):
        self.base_click(page.address_add_new_btn)

    # 输入收件人
    def page_input_receipt_name(self, name):
        self.base_input(page.address_receipt_name, name)

    # 输入手机号
    def page_input_add_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 点击 所在地区
    def page_click_capital(self):
        self.base_click(page.address_capital)

    # 选择 省/直辖市
    def page_click_province(self, pro):
        self.base_text_click(pro)

    # 选择市
    def page_click_city(self, city):
        self.base_text_click(city)

    # 选择 区
    def page_click_district(self, dis):
        self.base_text_click(dis)

    # 输入 详细地址
    def page_input_detail_addr_info(self, info):
        self.base_input(page.address_detail_addr_info, info)

    # 输入 邮编
    def page_input_post_code(self, code):
        self.base_input(page.address_post_code, code)

    # 设为默认地址
    def page_set_default_address(self):
        self.base_click(page.address_default)

    # 点击 保存
    def page_click_save(self):
        self.base_click(page.address_btn_send)

    # 获取 地址列表中 收件人、电话列表
    def page_get_receipt_list(self):
        return [i.text for i in self.base_finds(page.receipt_name_list)]

    # 获取 地址列表中 地址
    def page_get_address_list(self):
        return [i.text for i in self.base_finds(page.address_info)]

    # 点击 编辑按钮
    def page_click_compile(self):
        self.base_click(page.address_compile)

    # 点击 修改
    def page_click_alter(self):
        self.base_click(page.address_alter)

    # 获取 toast消息
    def page_get_toast(self, msg):
        self.base_get_toast(msg)

    # 点击删除
    def page_click_delete(self):
        self.base_click(page.address_delete)

    # 确认删除
    def page_click_delete_ok(self):
        self.base_click(page.address_delete_ok)

    # 判断地址列表中是否存在地址
    def page_if_address_exists(self):
        try:
            self.base_find(page.receipt_name_list, timeout=2)
            # 未删除干净
            return False
        except:
            return True


    # 组合业务方法--新增地址
    def page_address(self, name, phone, pro, city, dis, info, code):
        self.page_click_address_add_new_btn()
        self.page_input_receipt_name(name)
        self.page_input_add_phone(phone)
        self.page_click_capital()
        self.page_click_province(pro)
        self.page_click_city(city)
        self.page_click_district(dis)
        self.page_input_detail_addr_info(info)
        self.page_input_post_code(code)
        self.page_set_default_address()
        self.page_click_save()

    # 组合业务方法--修改地址
    def page_address_compile(self, name, phone, pro, city, dis, info, code):
        self.page_click_compile()
        self.page_click_alter()
        self.page_input_receipt_name(name)
        self.page_input_add_phone(phone)
        self.page_click_capital()
        self.page_click_province(pro)
        self.page_click_city(city)
        self.page_click_district(dis)
        self.page_input_detail_addr_info(info)
        self.page_input_post_code(code)
        self.page_click_save()

    # 组合业务方法--删除单个地址
    def page_delete_one(self):
        self.page_click_compile()
        self.page_click_delete()
        self.page_click_delete_ok()

    # 组合业务方法--删除所有地址
    def page_delete_all(self):
        for i in range(len(self.page_get_address_list())):
            self.page_click_compile()
            self.page_click_delete()
            self.page_click_delete_ok()