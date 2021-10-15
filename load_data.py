# DB에 주어진 csv데이터를 넣는 python 또는 sql을 실행
import csv
from datetime import date, datetime

from db_connect import db
from models import Movie

session = db.session

with open('oscar_award_data.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        movie = Movie(
            # id=int(row['id']),
            movie_name=row['movie_name'],
            ranking=row['ranking'],
            award_year=int(row['award_year']),
            award_name1=row['award_name1'],
            award_name2=row['award_name2'],
            award_name3=row['award_name3'],
            award_name4=row['award_name4'],
            award_name5=row['award_name5'],
            award_name6=row['award_name6'],
            award_name7=row['award_name7'],
            release_year=int(row['release_year']),
            running_time=row['running_time'],
            storyline=row['storyline'],
            user_rating=float(row['user_rating']),
            critic_rating=float(row['critic_rating']),
            genre1=row['genre1'],
            genre2=row['genre2'],
            genre3=row['genre3'],
            genre4=row['genre4'],
            genre5=row['genre5'],
            genre6=row['genre6'],
            genre7=row['genre7'],
            img_url=row['imgurl'],
        )
        db.session.add(movie)
    db.session.commit()
