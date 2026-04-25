# Flask 메인 애플리케이션: URL 라우팅과 데이터베이스 연결을 담당
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# 데이터베이스 파일 경로 (이 스크립트와 같은 폴더에 위치)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog.db")


def get_db():
    """데이터베이스 연결을 생성하고 행을 딕셔너리처럼 접근할 수 있게 설정"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def post_list():
    """글 목록 페이지: 모든 글을 최신순으로 가져와서 list.html에 전달"""
    conn = get_db()
    posts = conn.execute("SELECT * FROM posts ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("list.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    """글 상세 페이지: URL에서 받은 post_id로 글 하나를 조회해서 detail.html에 전달"""
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        return "글을 찾을 수 없습니다.", 404
    return render_template("detail.html", post=post)


@app.route("/write", methods=["GET", "POST"])
def write_post():
    """글쓰기 페이지: GET은 폼 보여주기, POST는 폼 데이터를 DB에 저장"""
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db()
        conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for("post_list"))
    return render_template("write.html")


if __name__ == "__main__":
    app.run(debug=True)
