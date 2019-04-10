import xadmin
from .models import EmailVerifyRecord,Banner, UserProfile
from django.contrib.auth.admin import UserAdmin
from xadmin import views

#xadmin的一些基础配置，也需要注册进xadmin当中；
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

# 修改页头页脚
class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"

class EmailVerifyRecordAdmin(object):
    list_display=['email','code','send_time','send_type']
    search_fields = ['code','email','send_type']
    list_filter = ['email','code','send_time','send_type']

class BannerAdmin(object):
    list_display=['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

class UserProfileAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

