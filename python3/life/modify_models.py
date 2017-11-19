source_dict = {'t_s_attachment': '系统上传附件表', 
                't_s_base_user': '系统用户基础表', 
                't_s_category': '系统分类表',   
                't_s_data_log': '业务数据日志表', 
                't_s_data_rule': '数据权限规则表', 
                't_s_data_source': '系统多数据源表', 
                't_s_depart': '系统组织机构',  
                't_s_function': '系统菜单权限',  
                't_s_icon': '系统图标',    
                't_s_log': '系统日志表',   
                't_s_muti_lang': '国际化语法表',  
                't_s_notice': '系统公告',    
                't_s_notice_authority_role': '系统公告角色关系表',   
                't_s_notice_authority_user': '系统公告人员关系表',   
                't_s_notice_read_user': '系统功能已读日志表',   
                't_s_operation': '系统操作权限',  
                't_s_role': '系统角色表',   
                't_s_role_function': '系统角色菜单关系表',   
                't_s_role_org': '系统角色组织机构关系表', 
                't_s_role_user': '系统角色用户关系表',   
                't_s_sms': '消息中心',    
                't_s_sms_sql': '消息中心SQL', 
                't_s_sms_template': '消息中心模板',  
                't_s_sms_template_sql': '消息中心模板SQL',   
                't_s_timetask': '定时任务表',   
                't_s_type': '字段表', 
                't_s_typegroup': '字典类别',    
                't_s_user': '用户表', 
                't_s_user_org': '用户组织机构关系表',   
                'cgform_button': 'Online表单自定义按钮',   
                'cgform_button_sql': 'Online表单SQL增强',   
                'cgform_enhance_java': 'Online表单Java增强',  
                'cgform_enhance_js': 'Online表单JS增强',    
                'cgform_field': 'Online表单字段',  
                'cgform_ftl': 'Online表单样式',  
                'cgform_head': 'Online表单主表',  
                'cgform_index': 'Online表单索引',  
                'cgform_template': 'Online表单模板',  
                'cgform_uploadfiles': 'Online表单上传文件',    
                'jform_cgdynamgraph_head': '移动报表配置主表',    
                'jform_cgdynamgraph_item': '移动报表配置明细',    
                'jform_cgdynamgraph_param': '移动报表配置参数',    
                'jform_cgreport_head': '动态报表主表',  
                'jform_cgreport_item': '动态报表字段',  
                'jform_cgreport_param': '动态报表参数',  
                'jform_graphreport_head': '移动图表配置主表',    
                'jform_graphreport_item': '移动图表配置字段',    
                't_s_region': '地域表', 
                'test_person': '测试用户表',   
                'jform_contact': '合同表', 
                'jform_contact_group': '通迅录分组',   
                'jform_employee_cost_claim': '员工费用报销申请信息表', 
                'jform_employee_entry': '员工入职单',   
                'jform_employee_leave': '员工请假单',   
                'jform_employee_meals_cost': '员工餐费明细表', 
                'jform_employee_other_cost': '员工其他费用明细表',   
                'jform_employee_resignation': '员工离职单',   
                'jform_leave': '请假单', 
                'jform_order_customer': '订单客户',    
                'jform_order_main': '订单主表',    
                'jform_order_ticket': '订单机票',    
                'jform_price1': '价格表', 
                'jform_resume_degree_info': '教育经历',    
                'jform_resume_exp_info': '工作信息表',   
                'jform_resume_info': '简历信息表',   
                'jform_tree': '树DEMO',   
                'jeecg_custom_info': '客户信息',    
                'jeecg_custom_record': '客户记录',    
                'jeecg_demo': '演示DEMO',  
                'jeecg_order_custom': '订单客户表',   
                'jeecg_order_main': '订单主表',    
                'jeecg_order_product': '订单产品表',   
                'jp_demo_activity': '插件活动表',   
                'jp_demo_auth': '插件树DEMO', 
                'jp_demo_order_custom': '插件订单客户表', 
                'jp_demo_order_main': '插件订单主表',  
                'jp_demo_order_product': '插件订单产品表', 
                'jp_inner_mail': '插件邮箱主表',  
                'jp_inner_mail_attach': '插件邮箱附件',  
                'jp_inner_mail_receiver': '插件邮件接收',  
                'chat_message_his': '在线聊天消息记录表'} 


def modify_data(data):
    for k,v in source_dict.items():
        data = data.replace("db_table = '%s'" % k, "db_table = '%s'\n        verbose_name_plural = '%s'" % (k, v,))

    return data


def rw_file():
    data = ''
    # 读取文件
    with open('/home/sdu/Documents/mysite/life/life/apps/base/models.py', 'rt') as f:
        data = f.read()

    data = modify_data(data)

    # 写入文件
    with open('/home/sdu/Documents/mysite/life/life/apps/base/models.py', 'wt') as f:
        f.write(data)


def main():
    rw_file()


if __name__ == '__main__':
    main()