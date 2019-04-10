from .models import UserMessage,UserAsk,UserCourse,UserFavorite
import xadmin

class UserMessageAdmin(object):
    pass

class UserAskAdmin(object):
    pass

class UserCourseAdmin(object):
    pass

class UserFavoriteAdmin(object):
    pass

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)