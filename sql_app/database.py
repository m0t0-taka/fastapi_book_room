# このファイルにはdatabaseの基本設定を記載する
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DBの格納先
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# 操作を行うための基盤を定義
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# DB接続の一連の流れの定義
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
