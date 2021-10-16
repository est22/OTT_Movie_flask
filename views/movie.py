from flask import redirect, request, render_template, jsonify, Blueprint, session, g, url_for, flash
from models import *
from datetime import datetime

api = Blueprint('movie', __name__, url_prefix='/')


@api.route('movieDetail/<int:movie_id>', methods=['GET',  'POST'])
def movie_detail(movie_id):
    '''
    parameter : year_id, movie_id
    GET : 해당 movie_id의 데이터 보여주기
    POST : 댓글
    '''

    # 해당 연도의 영화들을 불러옴
    movie_info = Movie.query.filter(Movie.id == movie_id).first()

    # 맞는 데이터가 없는 경우
    if movie_info is None:
        flash('영화를 찾을 수 없습니다.')
        return redirect('/')

    # 댓글 작성시 form post로 받음
    if request.method == 'POST':
        content = request.form['review']
        review_rating = int(request.form['rating'])
        now = datetime.now()
        write_time = now.strftime('%Y-%m-%d %H:%M:%S')

        # 댓글 내용과 별점이 없는 경우
        if not content:
            flash('댓글 내용을 작성해주세요.')
            return redirect(f'movieDetail/{movie_id}')
        if not rating:
            flash('별점을 선택해주세요.')
            return redirect(f'movieDetail/{movie_id}')

        # 댓글 작성이 올바르게 된 경우 : review table에 추가
        review_data = Review(
            user_name=session['user_name'], write_time=write_time, content=content, rating=review_rating, movie_id=movie_id)

        db.session.add(review_data)
        db.session.commit()

    # 지금까지 작성된 댓글을 최신순(desc)으로 가져온다 (if_post문에 포함되지 않음)
    # review_list = Review.query.filter(
        # Review.movie_id == movie_id).order_by(Review.write_time.desc()).all()

    review_list = Review.query.filter(
        Review.id == movie_id).order_by(Review.write_time.desc()).all()

    return render_template('movie_detail.html', movie_detail=movie_info, review_list=review_list)


# @api.route('movies/<int:movie_id>/like', methods=['GET', 'POST'])
# def likeMovies():
#     '''
#     parameter : movie_id
#     GET : 없음
#     POST : (하트버튼 클릭시) likeMovie 테이블에 데이터 저장
#     '''
#     # 영화 아이디와 맞는 데이터를 가져온다
#     movie_data = Movie.query.filter(Movie.id == movie_id).first()

#     # 맞는 데이터가 없는 경우
#     if movie_data is None:
#         flash('영화를 찾을 수 없습니다.')
#         return redirect('/')

#     # 이미 좋아요 버튼을 누른 영화인 경우
#     like_info = LikeMovie.query.filter(LikeMovie.movie_id == movie_id).filter(
#         LikeMovie.user_name == session['user_name']).all()
#     for movie in like_info:
#         if movie.movie_id == int(movie_id):
#             flash('이미 좋아요 한 영화입니다.')
#             return redirect('/mypage')

#     return


# @api.route('movies/<int:movie_id>/review', methods=['POST'])
# def create_movieReview():
#     '''
#     parameter : movie_id
#     GET : 없음
#     POST : (댓글 작성시) review 테이블에 데이터 저장
#     '''
#     # 영화 아이디와 맞는 데이터를 가져온다
#     movie_data = Movie.query.filter(Movie.id == movie_id).first()

#     # 맞는 데이터가 없는 경우
#     if movie_data is None:
#         flash('영화를 찾을 수 없습니다.')
#         return redirect('/')

#     # 댓글 작성시 form post로 받음
#     if request.method == 'POST':
#         now = datetime.now()
#         write_time = now.strftime('%Y-%m-%d %H:%M:%S')
#         content = request.form['review']
#         review_rating = int(request.form['rating'])

#         # 댓글 내용과 별점이 없는 경우
#         if not content:
#             # flash('댓글 내용을 작성해주세요.')
#             return redirect(f'/{movie_id}')
#         if not rating:
#             # flash('별점을 선택해주세요.')
#             return redirect(f'/{movie_id}')

#         # 댓글 작성이 올바르게 된 경우 : review table에 추가
#         review_data = Review(
#             user_name=session['user_name'], write_time=write_time, content=content, rating=rating, movie_id=movie_id)

#         db.session.add(review_data)
#         db.session.commit()

#     # 지금까지 작성된 댓글을 최신순(desc)으로 가져온다 (if_post문에 포함되지 않음)
#     review_list = Review.query.filter(
#         Review.movie_id == movie_id).order_by(Review.write_time.desc()).all()

#     return review_list
#     # render_template('~.html', review_list=review_list)


# # @api.route('movies/<int:movie_id>/review/<int:review_id>', methods=['GET', 'POST'])
# # def delete_movieReview():
# #     '''
# #     parameter : movie_id, review_id
# #     GET :
# #     POST :
# #     '''
# #     return
