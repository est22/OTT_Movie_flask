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
    # if request.method == 'POST':
    #     year_id = request.form['award_year']

    #     # year_id 가 없는 경우
    #     if not year_id:
    #         flash('year_id는 필수 파라미터 입니다.')
    #         return render_template("main.html")
    #     year_list = Movie.query.filter(Movie.award_year == year_id).all()
    #     return render_template("movies.html", year_id=year_list.award_year)

    # GET방식인 경우
    return render_template("main.html")


@api.route("years/<int:year_id>", methods=['GET', 'POST'])
def movies(year_id):
    '''
    GET : 해당 year_id에 맞는 movies.html 보여주기
    POST : 없음
    '''
    # 해당 연도 영화 데이터를 불러옴
    year_movie_list = Movie.query.filter(
        Movie.award_year == year_id).all()
    # 맞는 데이터가 없는 경우
    if year_movie_list is None:
        flash(f'{year_id}연도의 영화를 찾을 수 없습니다.')
        return redirect('/')

    # if request.method == 'POST':
    #     movie_id = request.form['movie_id']

    #     # 영화 정보
    #     movie_info = Movie.query.filter(Movie.id == movie_id).first()

    #     if movie_info is None:
    #         flash('해당 영화를 찾을 수 없습니다.')
    #         return render_template("movies.html", year_movie_list=year_movie_list)

    #     return render_template("movie_detail.html", movie_detail=movie_detail, review_list=review_list)

    # GET방식인 경우
    return render_template("movies.html", year_movie_list=year_movie_list)


#

#     review_list = Review.query.filter(
#         Review.movie_id == movie_id).order_by(Review.write_time.desc()).all()

#     return render_template('movie_detail.html', movie_detail=movie_info, review_list=review_list)
