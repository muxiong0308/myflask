from flask import render_template, request, url_for
from flask import redirect, flash
from apps.Auth.forms import LoginForm, RegiForm
from apps.Auth.model import User, UserDao
from flask_login import login_required, login_user, logout_user
from apps import login_manager
from apps.common import Common


def query_user(user_id):
    return UserDao.get_byId(UserDao, user_id)


def init_route(app):
    @app.route('/regi/', methods=['POST', 'GET'])
    def regi():
        # POST请求
        form = RegiForm(request.form)
        if request.method == 'POST' and form.validate():
            user_id = request.form['user_id']
            user_name = request.form['user_name']
            user_pswIn = request.form['password']
            userVo = query_user(user_id)

            if (userVo is None):
                curr_user = UserDao(user_id=user_id,
                                    user_name=user_name,
                                    user_password=user_pswIn)
                daoRes = UserDao.add(UserDao, curr_user)
                if (daoRes is None):
                    flash('注册成功')
                    return redirect(url_for('login'))
                else:
                    flash('数据入库有误：' + daoRes)
            else:
                flash('用户已存在')
        # GET请求
        return render_template('regi.html', form=form)

    @app.route('/login/', methods=['POST', 'GET'])
    def login():
        # POST请求
        if request.method == 'POST':
            user_id = request.form['user_id']
            user_pswIn = request.form['password']
            userVo = query_user(user_id)

            if (userVo is not None and Common.encryptedPsw(
                    user_pswIn,
                    userVo.salt) == userVo.password):
                curr_user = User()
                curr_user.id = user_id
                login_user(curr_user, remember=True)
                # # TODO 建议对next参数值作验证，避免被URL注入攻击
                # next = request.args.get('next')
                # return redirect(next or url_for('index'))
                return redirect(url_for('index'))
            flash('账号或密码错误')
        # GET请求
        form = LoginForm()
        return render_template('login.html', form=form)

    @app.route('/logout/')
    @login_required
    def logout():
        logout_user()
        return 'Logged out successfully!'

    @login_manager.user_loader
    def load_user(user_id):
        if query_user(user_id) is not None:
            curr_user = User()
            curr_user.id = user_id
            return curr_user
