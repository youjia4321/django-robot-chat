from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect
from robot.forms import LoginForm
from robot.views import check
from django.contrib.auth import login, logout

class DealLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("MD1里面的 process_request")

    def process_response(self, request, response):
        print("MD1里面的 process_response")
        '''
            if not request.user.is_authenticated:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                user = check(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {'msg': "用户不存在或密码错误"})
            else:
                return render(request, 'login.html', {'login_form': login_form})
                
        这样写还没解决就是注册用户时,中间件运行时不会跳到注册页面
        '''
        return response

    # view_func是Django即将使用的视图函数。 （它是实际的函数对象，而不是函数的名称作为字符串。）
    # view_args是将传递给视图的位置参数的列表.
    # view_kwargs是将传递给视图的关键字参数的字典。 view_args和view_kwargs都不包含第一个视图参数（request）。
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("-" * 80)
        print("MD1里面的 process_view")
        print("-" * 80)

        
    def process_exception(self, request, exception):
        print(exception)
        print("MD1 中的process_exception")
        return HttpResponse(str(exception))

    def process_template_response(self, request, response):
        print("MD1 中的process_template_response")
        return response


# # class MD2(MiddlewareMixin):
# #     def process_request(self, request):
# #         print("MD2里面的 process_request")
# #         pass

# #     def process_response(self, request, response):
# #         print("MD2里面的 process_response")
# #         return response

# #     def process_view(self, request, view_func, view_args, view_kwargs):
# #         print("-" * 80)
# #         print("MD2 中的process_view")
# #         print(view_func, view_func.__name__)
# #         print("-" * 80)

# #     def process_exception(self, request, exception):
# #         print(exception)
# #         print("MD2 中的process_exception")

# #     # process_template_response是在视图函数执行完成后立即执行，但是它有一个前提条件，那就是视图函数返回的对象有一个render()
# #     # 方法（或者表明该对象是一个TemplateResponse对象或等价方法）。
# #     def process_template_response(self, request, response):
# #         print("MD2 中的process_template_response")
# #         return response
