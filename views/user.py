from flask import redirect, request, render_template, jsonify, Blueprint, session, g, url_for, flash
from models import *
from datetime import datetime

api = Blueprint('user', __name__, url_prefix='/user')


@api.route('/favorites', methods=['GET'])
def favorites():
    '''
    GET : 해당 user가 좋아하는 영화 리스트 데이터를 반환
    POST : 없음 (해당 영화 클릭시 영화의 페이지로 이동하도록 - front)
    '''
    like_list = LikeMovie.query.filter(
        LikeMovie.user_name == session['user_name']).all()

    like_movie_id = review_list.movie_id

    return like_movie_id


@api.route('/reviews', methods=['GET', 'POST'])
def reviews():
    '''
    GET : 해당 user가 작성한 모든 리뷰 데이터를 (어느영화든 상관없이) 전부 가져온다.
    POST : (그 페이지에서) 리뷰 삭제
    '''
    # 사용자 작성 리뷰 테이블에서
    # 현재 세션 username과 db의 username이 동일한 것을 골라서 모든 movie_id를 출력한다
    if request.method == 'GET':
        review_list = Review.query.filter(
            Review.user_name == serssion['username']).order_by(Review.write_time.desc()).all()
        review_movie_id = review_list.movie_id

        # User.query.filter((User.email == email) | (User.name == name)).first()

        return review_movie_id

    # # 유튜브 댓글 모아서 삭제 로직 참고
