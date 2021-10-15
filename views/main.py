from flask import redirect, request, render_template, jsonify, Blueprint, session, g, url_for, flash
from models import *
from datetime import datetime

api = Blueprint('movie', __name__, url_prefix='/')


@api.route("/", methods=['GET', 'POST'])
def main():
    # 대여하기 버튼 클릭시
    if request.method == 'POST':
        year_id = request.form['year_id']

        # year_id 가 없는 경우
        if not year_id:
            flash('year_id는 필수 파라미터 입니다.')
            return render_template("main.html")
        else:
            year_list = Movie.query.filter(Movie.award_year == year_id).all()

        return render_template("movies.html", year_list=year_list)

    # GET방식인 경우
    return render_template("main.html")
