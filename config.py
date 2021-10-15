import os
# 폴더 구조가 달라져도, 현재 폴더를 가져와서 사용할 수 있도록 설정
BASE_DIR = os.path.dirname(__file__)

# mysql://<id>:<password>@<server url host>:<server url port>/<db name>
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1124@localhost:3306/oscar_award'
# 메모리 사용량을 위해서 꺼둠
SQLALCHEMY_TRACK_MODIFICATIONS = False
