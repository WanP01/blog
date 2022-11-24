"""采用django addmin 后台时需要限制用户权限"""
import re

from django.http import HttpResponse


class URLPermitMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):

        #view视图之前的代码
        # print('view之前')

        # 避免陷入死循环（要排除login，register页面的middleware检测）
        exclude_middleware = r'(login)|(register)'
        # print(request.path_info)
        re_url = re.compile(exclude_middleware)
        # print(re_url.search(request.path_info))
        if not re_url.search(request.path_info):
        # 当前仅允许访问个人文件夹以及文章修改页面
            permit_URL = r'(admin/user/userinfo/(%s)/change)|(admin/mainblog/post/)'%request.user_id
            # print(request.path_info)
            re_url = re.compile(permit_URL)
            # print(re_url.search(request.path_info))
            # print(re.search('admin',request.path_info))
            if not request.is_staff:
                if re.search('admin',request.path_info) and not re_url.search(request.path_info):
                    return HttpResponse('你没有网页权限，请联系管理员')

        response = self.get_response(request)

        #view视图之后的代码
        # print('view 之后')

        return response