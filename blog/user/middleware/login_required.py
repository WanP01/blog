from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import re
from user.models import UserInfo


class LoginRequireMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):

        #view视图之前的代码
        # print('view之前')
        #避免陷入死循环（要排除login，register页面的middleware检测）
        exclude_middleware = r'(login)|(register)'
        # print(request.path_info)
        re_url = re.compile(exclude_middleware)
        # print(re_url.search(request.path_info))
        if not re_url.search(request.path_info):
            if not request.session.get('is_login',None):
                return HttpResponseRedirect(reverse('user:login'))
            else:
                request.is_login = request.session.get('is_login',None)
                request.user_name = request.session.get('user_name', None)
                request.is_staff = UserInfo.objects.get(username=request.user_name).is_staff
                request.user_id = UserInfo.objects.get(username=request.user_name).id
                # print(request.is_login)
                # print(request.user_id)
                # print(request.user_name)

        response = self.get_response(request)

        #view视图之后的代码
        # print('view 之后')

        return response

