from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length


# 定义的表单都需要继承自FlaskForm
# 登录页
class LoginForm(FlaskForm):
    # 域初始化时，第一个参数是设置label属性的
    user_id = StringField('操作号',
                          validators=[
                              DataRequired(),
                              Length(min=5,
                                     max=8,
                                     message="请输入长度为%(min)d-%(max)d位的操作号")
                          ],
                          render_kw={"placeholder": "请输入操作号"})
    password = PasswordField('密码',
                             validators=[
                                 DataRequired(),
                                 Length(min=6,
                                        max=16,
                                        message="请输入长度为%(min)d%(max)d位的密码")
                             ],
                             render_kw={"placeholder": "请输入密码"})


# 注册页
class RegiForm(FlaskForm):
    user_id = StringField('操作号',
                          validators=[
                              DataRequired(),
                              Length(min=5,
                                     max=8,
                                     message="请输入长度为%(min)d-%(max)d位的操作号")
                          ],
                          render_kw={"placeholder": "请输入5-8位操作号"})
    user_name = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码',
                             validators=[
                                 DataRequired(),
                                 Length(min=6,
                                        max=16,
                                        message="请输入长度为%(min)d-%(max)d位的密码")
                             ],
                             render_kw={"placeholder": "请输入6-16位密码"})
    confrimPsw = PasswordField('再次输入密码',
                               validators=[
                                   DataRequired(),
                                   EqualTo('password', message='两次输入密码不一致'),
                               ])
