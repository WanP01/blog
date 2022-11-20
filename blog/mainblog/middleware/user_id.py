import uuid

USER_KEY = 'uid'

TEN_YEARS = 60*60*24*365*10

class UserIDMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        #尝试获取uid
        uid = self.generate_id(request)
        #把uid赋予request，用于后期View调用
        request.uid = uid
        #获取对应request的response数据
        response= self.get_response(request)
        # 在response 里保存cookie给浏览器
        response.set_cookie(USER_KEY,uid,max_age=TEN_YEARS,httponly=True)
        return response

    #判断是否cookie里是否有uid
    def generate_id(self,request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4()
        return uid

