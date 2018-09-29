from crm import models
from stark.service.stark import site, StarkConfig,Option
from django.utils.safestring import mark_safe
from django.conf.urls import url
from django.shortcuts import HttpResponse
from django.urls import reverse


class ClassListConfig(StarkConfig):   #这里放的是stark配置文件，配置好以后，每个功能增加至少增删改查四个路由

    def display_title(self, row=None, header=False):
        if header:
            return '班级'
        return "%s-%s期" % (row.course.name, row.semester)

    def display_start_date(self, row=None, header=False):
        if header:
            return '开班日期'
        return row.start_date.strftime('%Y-%m-%d')

    list_display = ['id', display_title, 'school', display_start_date, StarkConfig.display_edit,
                    StarkConfig.display_del]    #显示字段，右边搜索框可以搜索到的内容


    list_filter = [
        Option(field='school',is_choice=False,is_multi=False,text_func=lambda x:x.title,value_func=lambda x:x.pk),
        Option(field='course',is_choice=False,is_multi=False,text_func=lambda x:x.name,value_func=lambda x:x.pk),
    ]
        #组合搜索，过滤字段。就是汽车之家最上面的 代码