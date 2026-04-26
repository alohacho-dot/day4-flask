import os
import sqlite3
import sys

import requests

from crawler import GOOGLE_NEWS_KO_RSS, fetch_rss, parse_rss_items


def get_db_path() -> str:
    env_db_path = os.environ.get("DB_PATH")
    if env_db_path:
        return env_db_path
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog.db")


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


def seed_posts(limit: int = 10) -> int:
    xml_text = fetch_rss(GOOGLE_NEWS_KO_RSS)
    items = parse_rss_items(xml_text, limit=limit)

    db_path = get_db_path()
    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    try:
        init_db(conn)

        inserted_count = 0
        for item in items:
            title = item["title"].strip()
            summary = item["summary"].strip()
            link = item["link"].strip()
            published_at = item["published_at"].strip()

            exists = conn.execute(
                "SELECT 1 FROM posts WHERE title = ? LIMIT 1",
                (title,),
            ).fetchone()

            if exists:
                continue

            content = (
                f"요약: {summary}\n"
                f"링크: {link}\n"
                f"발행시간: {published_at}"
            )

            conn.execute(
                "INSERT INTO posts (title, content) VALUES (?, ?)",
                (title, content),
            )
            inserted_count += 1

        conn.commit()
        return inserted_count
    finally:
        conn.close()


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    try:
        inserted = seed_posts(limit=10)
        print(f"{inserted}건 추가됨")
    except requests.RequestException as e:
        print(f"RSS 요청 실패: {e}")


if __name__ == "__main__":
    main()
