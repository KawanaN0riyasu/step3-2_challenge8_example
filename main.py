from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# データベースの設定
DATABASE_URL = 'sqlite:///sample.db'
Base = declarative_base()

# テーブルを定義
class DataLog(Base):
    __tablename__ = 'data_log'
    timestamp = Column(String, primary_key=True)

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def log_current_time(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"データを取得しています... {current_time}")
    new_log = DataLog(timestamp=current_time)
    session.add(new_log)
    session.commit()
    session.close()

if __name__ == "__main__":
    engine = create_database()
    log_current_time(engine)