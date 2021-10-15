from flask import redirect, request, render_template, jsonify, Blueprint, session, g, url_for, flash
from models import *
from datetime import datetime

api = Blueprint('main', __name__, url_prefix='/')


@api.route("/", methods=['GET', 'POST'])
def main():
    '''
    GET : movie 테이블의 award_year를 보여주기 (db연동 안하고 그냥 html에서 연도 작성)
    POST : html의 form으로 들어오는 award_year를 기준으로 해당 영화 리스트 
    '''
    # 대여하기 버튼 클릭시
    if request.method == 'POST':
        year_id = request.form['award_year']

        # year_id 가 없는 경우
        if not year_id:
            flash('year_id는 필수 파라미터 입니다.')
            return render_template("main.html")
        year_list = Movie.query.filter(Movie.award_year == year_id).all()
        return render_template("movies.html", year_id=year_list)

    # GET방식인 경우
    return render_template("main.html")


@api.route("years/<int:year_id>", methods=['GET', 'POST'])
def movie_list():
    book_list = LibraryBook.query.all()
