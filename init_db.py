# SQLite 데이터베이스를 만들고 posts 테이블을 초기화하는 스크립트
import sqlite3
import os

DB_NAME = "blog.db"


def get_db_path():
    # 이 스크립트가 있는 폴더에 blog.db 파일을 생성
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)


def init_db():
    conn = sqlite3.connect(get_db_path())
    cur = conn.cursor()

    # posts 테이블 생성 (이미 있으면 건너뜀)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print(f"데이터베이스 초기화 완료: {get_db_path()}")


if __name__ == "__main__":
    init_db()
