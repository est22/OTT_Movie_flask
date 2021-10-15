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
    if request.method == 'POST':
        year_id = request.form['award_year']

        # year_id 가 없는 경우
        if not year_id:
            flash('year_id는 필수 파라미터 입니다.')
            return render_template("main.html")
        year_list = Movie.query.filter(Movie.award_year == year_id).all()
        return render_template("movies.html", year_id=year_list.award_year)

    # GET방식인 경우
    return render_template("main.html")


@api.route("years/<int:year_id>", methods=['GET', 'POST'])
def movies(year_id):
    '''
    GET : 해당 year_id에 맞는 movies.html 보여주기
    POST : movie_id 넘겨주기
    '''
    year_list = Movie.query.filter(Movie.award_year == year_id).all()
    movie_id = year_list.id
    if request.method == 'POST':
        movie_id = request.form['movie_id']
        # 영화 정보
        movie_info = Movie.query.filter(Movie.id == movie_id).first()

        if movie_info is None:
            flash('해당 영화를 찾을 수 없습니다.')
            return render_template("movies.html", movie_list=year_list)

        # review_list = Review.query.filter(
        # Review.book_id == book_id).order_by(Review.write_time.desc()).all()

        # return render_template("movie_detail.html", )

    # GET방식인 경우
    return render_template("movies.html", movie_list=year_list)
