# _*_ coding=utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import UserMessage
from .forms import LoginForm, RegisterForm, ForgetForm
from userinfo import generat_captcha
import re
import os
from txy import settings



# class LoginView(View):
#     def get(self, request):
#         return render(request, "crowdfunding.html", {})
#
#     def post(self, request):
#         user_name = request.POST.get("username")
#         pass_word = request.POST.get("password")
#
#         if user_name == "":
#             return render(request, "crowdfunding.html", {"logined":"0","msg":"用户名不能为空"})
#         elif pass_word == "":
#             return render(request, "crowdfunding.html", {"logined":"0","msg":"密码不能为空"})
#         else:
#             name_pw_massage = UserMessage.objects.filter(username=user_name)
#             email_pw_massage = UserMessage.objects.filter(email=user_name)
#             if name_pw_massage:
#                 for name_pw_msg in name_pw_massage:
#                     pw = name_pw_msg.password
#                 if pw == pass_word:
#                     request.session["username"] = user_name
#                     return render(request, "crowdfunding.html", {"logined": "1", "msg":user_name})
#                 else:
#                     return render(request, "crowdfunding.html", {"logined": "0", "msg": "密码错误"+user_name})
#
#             elif email_pw_massage:
#                 for email_pw_msg in email_pw_massage:
#                     pw = email_pw_msg.password
#                 if pw == pass_word:
#                     request.session["username"] = user_name
#                     return render(request, "crowdfunding.html",{"logined": "1", "msg": user_name})
#                 else:
#                     return render(request, "crowdfunding.html", {"logined": "0", "msg": "密码错误"})
#             else:
#                 return render(request, "crowdfunding.html", {"logined": "0", "msg": "用户名不存在" + name_pw_massage})


class RegisterView(View):
    captcha = '0'

    def get(self, request,registform = {}):
        RegisterView.captcha = generat_captcha.gen_captcha_text_and_image()#生成验证码
        return render(request, "regist.html", registform)

    def post(self, request):

        regist_error = {}#检查输入字符的合法性
        auto_input_form = {}#当注册时某一项出错时，第二次注册时将未出错项自动填入

        input_username = request.POST.get("username")
        input_password = request.POST.get("password")
        input_confirm_password = request.POST.get("confirm_password")
        input_user_realname = request.POST.get("user_realname")
        input_user_email = request.POST.get("user_email")
        input_user_id_card_number = request.POST.get("user_id_card_number")
        input_user_mobile = request.POST.get("user_mobile")
        input_user_qq = request.POST.get("user_qq")
        input_user_home_adress = request.POST.get("user_home_adress")
        input_user_company_name = request.POST.get("user_company_name")
        input_captcha = request.POST.get("captcha")
        is_agree_rule = request.POST.get("agree_rule")

        
        username_list = []
        user_email_list = []
        user_id_card_number_list = []
        user_qq_list = []
        user_mobile_list = []

        all_message = UserMessage.objects.all()
        for message in all_message:
            username_list.append(message.username)
            user_email_list.append(message.user_email)
            user_id_card_number_list.append(message.user_id_card_number)
            user_qq_list.append(message.user_qq)
            user_mobile_list.append(message.user_mobile)


        if input_username == "":
            regist_error["username_error"] = "此项不能为空"
        elif input_username in username_list:
            regist_error["username_error"] = "用户名已存在"
        else:
            auto_input_form["auto_input_username"] = input_username

        if input_password == "":
            regist_error["password_error"] = "此项不能为空"
        elif input_password.isalnum() != True or len(input_password) < 8:
            regist_error["password_error"] = "密码必须为8位以上，且不得含有特殊字符"
        else:
            auto_input_form["auto_input_password"] = input_password

        if input_confirm_password == "":
            regist_error["confirm_password_error"] = "此项不能为空"
        elif input_password != input_confirm_password:
            regist_error["confirm_password_error"] = "两次密码输入不一致"
        else:
            auto_input_form["auto_input_confirm_password"] = input_confirm_password

        if input_user_realname == "":
            regist_error["user_realname_error"] = "此项不能为空"
        elif re.search("[\u4e00-\u9fa5]{2,}", input_user_realname) is None:
            regist_error["user_realname_error"] = "请输入正确的中文姓名"
        else:
            auto_input_form["auto_input_user_realname"] = input_user_realname

        if input_user_email == "":
            regist_error["user_email_error"] = "此项不能为空"
        elif re.search("^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$", input_user_email) is None:
            regist_error["user_email_error"] = "请检查邮箱是否输入正确"
        elif input_user_email in user_email_list:
            regist_error["user_email_error"] = "此邮箱已被注册"
        else:
            auto_input_form["auto_input_user_email"] = input_user_email

        if input_user_id_card_number == "":
            regist_error["user_id_card_number_error"] = "此项不能为空"
        elif re.search('^(\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)',input_user_id_card_number) is None:
            regist_error["user_id_card_number_error"] = "请检查身份证号是否输入正确"
        elif input_user_id_card_number in user_id_card_number_list:
            regist_error["user_id_card_number_error"] = "此身份证号已被注册"
        else:
            auto_input_form["auto_input_user_id_card_number"] = input_user_id_card_number

        if input_user_mobile == "":
            regist_error["user_mobile_error"] = "此项不能为空"
        elif re.search("^^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7}",input_user_mobile) is None:
            regist_error["user_mobile_error"] = "请检查手机号码是否输入正确"
        elif input_user_mobile in user_mobile_list:
            regist_error["user_mobile_error"] = "此手机号码已被注册"
        else:
            auto_input_form["auto_input_user_mobile"] = input_user_mobile

        if input_user_qq == "":
            regist_error["user_qq_error"] = "此项不能为空"
        elif re.search("[1-9][0-9]{4,10}$",input_user_qq) is None or len(input_user_qq) >11:
            regist_error["user_qq_error"] = "请检查QQ号码是否输入正确"
        elif input_user_qq in user_qq_list:
            regist_error["user_qq_error"] = "此QQ号已被注册"
        else:
            auto_input_form["auto_input_user_qq"] = input_user_qq

        if input_user_home_adress == "":
            regist_error["user_home_adress_error"] = "此项不能为空"
        else:
            auto_input_form["auto_input_user_home_adress"] = input_user_home_adress

        if input_user_company_name == "":
            regist_error["user_company_name_error"] = "此项不能为空"
        else:
            auto_input_form["auto_input_user_company_name"] = input_user_company_name

        if input_captcha == "":
            regist_error["captcha_error"] = "此项不能为空"
        elif input_captcha != RegisterView.captcha:
            regist_error["captcha_error"] = "验证码错误"

        if is_agree_rule == None:
            regist_error["agree_rule_error"] = "未同意条款"

        if regist_error != {} :
            auto_input_form_and_regist_error = dict(auto_input_form,**regist_error)
            return self.get(request,auto_input_form_and_regist_error)
            # return render(request,'regist.html',auto_input_form_and_regist_error)


        else:#if regist_error == {}
            try:
                UserMessage.objects.create(username = input_username,
                                           password = input_password,
                                           user_realname = input_username,
                                           user_email=input_user_email,
                                           user_id_card_number=input_user_id_card_number,
                                           user_mobile=input_user_mobile,
                                           user_qq=input_user_qq,
                                           user_home_address=input_user_home_adress,
                                           user_company_name=input_user_company_name
                                           )
                request.session['username'] = input_username
                login_form = {"logined": "1", "msg": input_username}
            except:
                return self.get(request)

            return render(request,'crowdfunding.html',login_form)


class ModifyMessageView(View):

    def get(self, request):
        username = request.session["username"]
        all_message = UserMessage.objects.filter(username=username)
        for message in all_message:
            return render(request, "personalcenter.html",{"username":username,
                                                          "user_gender":message.user_gender,
                                                          "user_signature":message.user_signature,
                                                          "user_mobile":message.user_mobile,
                                                          "user_hand_portrait":message.user_hand_portrait
                                                          })

    def post(self, request):
        #添加两个错误处理，可以使两个form分开提交
        try:
            username = request.session["username"]

            input_username = request.POST.get("username")
            input_user_signature = request.POST.get("user_signature")
            input_user_mobile = request.POST.get("user_mobile")
            input_user_gender = request.POST.get("user_gender")

            username_list = []
            user_mobile_list = []

            all_message = UserMessage.objects.all()
            for message in all_message:
                username_list.append(message.username)
                user_mobile_list.append(message.user_mobile)

            if input_username != "" and input_username not in username_list and input_username != None:
                UserMessage.objects.filter(username=username).update(username = input_username)
                request.session["username"] = input_username
            if input_user_signature != "" and input_user_signature != None:
                UserMessage.objects.filter(username=username).update(user_signature= input_user_signature)
            if input_user_mobile != "" and input_user_mobile!= None and re.search("^^(13\d|14[57]|15[^4\D]|17[13678]|18\d)\d{8}|170[^346\D]\d{7}",input_user_mobile) is not None and input_user_mobile not in user_mobile_list:
                UserMessage.objects.filter(username=username).update(user_mobile=input_user_mobile)
            if input_user_gender != "" and input_user_gender !=None:
                UserMessage.objects.filter(username=username).update(user_gender=input_user_gender)
        except:
            pass


        try:
            if request.method == "POST":
                username = request.session["username"]
                user_hand_portrait = request.FILES['user_hand_portrait']
                user_hand_portrait_path = os.path.join(settings.MEDIA_ROOT, 'user_hand_portrait',request.session['username']+'_hand_portrait.jpg')
                with open(user_hand_portrait_path, 'wb') as pic:
                    for c in user_hand_portrait.chunks():
                        pic.write(c)
                UserMessage.objects.filter(username=username).update(user_hand_portrait=os.path.join('user_hand_portrait',request.session['username']+'_hand_portrait.jpg'))
        except:
            pass

        return self.get(request)