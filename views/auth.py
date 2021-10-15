from flask import redirect, request, render_template, jsonify, Blueprint, session, g, url_for, flash
from models import *
from flask_bcrypt import Bcrypt
# from werkzeug.security import generate_password_hash, check_password_hash   # Bcrypt에 포함되어있음
from flask_login import login_required, login_user, current_user, logout_user

api = Blueprint('auth', __name__, url_prefix='/')
bcrypt = Bcrypt()


@api.route('/register', methods=['GET', 'POST'])
def register():
    '''
    GET : 회원가입
    POST : user db와 비교해서 새로운 유저 생성
    '''
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        password2 = request.form['password2']

        # 이름 입력 안됨
        if not user_name:
            # flash('이름을 입력해주세요.')
            return render_template('register.html')
            # return jsonify({"result": "user name none"})

        # 비밀번호가 없음
        if not password or not password2:
            # flash('비밀번호를 입력해주세요.')
            # return render_template('register.html')
            return jsonify({"result": "password null"})

        # 비밀번호가 일치하지 않음
        if password != password2:
            # flash('비밀번호가 일치하지 않습니다.')
            return render_template('register.html')

        # 비밀번호 암호화
        pw_hash = bcrypt.generate_password_hash(password)

        # 사용자 중복 확인
        user_check = User.query.filter(
            User.user_name == user_name).first()
        if user_check:
            # flash("이미 존재하는 닉네임입니다. 다른 이름을 입력해주세요.")
            return render_template('register.html')
            # return jsonify(result='email_check')

        # db에 유저 생성
        user_data = User(user_name=user_name, password=pw_hash)
        db.session.add(user_data)
        db.session.commit()

        # flash("회원가입이 완료되었습니다. 로그인해주세요!😊")
        return redirect("/login")

    # get방식인 경우
    # return jsonify({"result": "user_none"})
    return render_template('register.html')


@api.route('/login', methods=["GET", "POST"])
def login():
    '''
    GET : 로그인
    POST : user db와 비교해서 로그인 성공
    '''
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']

        # front에서도 가능
        if not user_name:
            # flash('닉네임을 입력해주세요.')
            return redirect("/login")
        if not password:
            # flash('비밀번호를 입력해주세요.')
            return redirect("/login")

        # 사용자 db가져오기
        user_data = User.query.filter(
            User.user_name == user_name).first()

        # 사용자 존재하는 경우
        if user_data is not None:

            # 암호화된 비밀번호 일치 여부
            if bcrypt.check_password_hash(user_data.password, password):
                # 세션 생성
                session.clear()
                session['user_name'] = user_data.user_name
                # flash("로그인 완료")
                return jsonify({"result": "success 로그인 완료 메인 페이지 보여줌"})

            # 비밀번호 일치하지 않음
            else:
                # flash("비밀번호를 다시 확인해주세요.")
                return jsonify({"result": "비번 없음"})

        # 사용자 없음
        else:
            flash("해당 닉네임이 없습니다. 회원가입해주세요.")
            # return redirect("/register")
            return jsonify({"result": "user_none"})

    else:  # GET
        return render_template('login.html')


@api.route('/logout', methods=["DELETE"])
def logout():
    '''
    로그아웃
    세션에서 사용자 정보 지워준다.
    '''
    session.clear()
    # flash("로그아웃 되었습니다.")
    return redirect("/")
