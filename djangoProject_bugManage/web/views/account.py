"""
用户账号相关功能：注册，登录，短信，注销 .etc.
"""
from django.shortcuts import render, HttpResponse
from web.forms.account import RegisterModelForm
from web.forms.account import SendSmsForm


def register(request):
    """注册"""
    form = RegisterModelForm()
    return render(request, 'web/register.html', {'form': form})


def send_sms(request):
    """发送短信"""
    form = SendSmsForm(data=request.GET)
    # 只是校验手机号:不能为空和格式是否正确
    if form.is_valid():
        pass
    return HttpResponse('成功')
