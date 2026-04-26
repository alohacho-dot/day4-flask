# Flask 메인 애플리케이션: URL 라우팅과 데이터베이스 연결을 담당
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)


def get_db_path():
    env_db_path = os.environ.get("DB_PATH")
    if env_db_path:
        return env_db_path
    if os.environ.get("RENDER"):
        return "/var/data/blog.db"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "blog.db")


DB_PATH = get_db_path()
db_dir = os.path.dirname(DB_PATH)
if db_dir:
    os.makedirs(db_dir, exist_ok=True)


def init_db():
    """posts 테이블이 없으면 생성 (Render 배포 시 자동 실행)"""
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


# 앱 시작 시 테이블 자동 생성
init_db()


def get_db():
    """데이터베이스 연결을 생성하고 행을 딕셔너리처럼 접근할 수 있게 설정"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def post_list():
    """글 목록 페이지: 검색 + 정렬 + 10개 단위 페이지네이션 목록 전달"""
    page = request.args.get("page", 1, type=int)
    if page < 1:
        page = 1

    q = request.args.get("q", "", type=str).strip()
    sort = request.args.get("sort", "latest", type=str)

    sort_map = {
        "latest": "created_at DESC, id DESC",
        "oldest": "created_at ASC, id ASC",
        "title": "title ASC",
    }
    if sort not in sort_map:
        sort = "latest"

    order_by = sort_map[sort]
    per_page = 10
    offset = (page - 1) * per_page

    conn = get_db()

    if q:
        like_q = f"%{q}%"
        total_count = conn.execute(
            "SELECT COUNT(*) FROM posts WHERE title LIKE ? OR content LIKE ?",
            (like_q, like_q)
        ).fetchone()[0]
    else:
        total_count = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]

    total_pages = max((total_count + per_page - 1) // per_page, 1)

    if page > total_pages:
        page = total_pages
        offset = (page - 1) * per_page

    if q:
        like_q = f"%{q}%"
        posts = conn.execute(
            f"SELECT * FROM posts WHERE title LIKE ? OR content LIKE ? ORDER BY {order_by} LIMIT ? OFFSET ?",
            (like_q, like_q, per_page, offset)
        ).fetchall()
    else:
        posts = conn.execute(
            f"SELECT * FROM posts ORDER BY {order_by} LIMIT ? OFFSET ?",
            (per_page, offset)
        ).fetchall()

    conn.close()

    return render_template(
        "list.html",
        posts=posts,
        current_page=page,
        total_pages=total_pages,
        q=q,
        sort=sort
    )


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


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    """글 수정 페이지: GET은 기존 글을 폼에 채워서 보여주기, POST는 DB 업데이트"""
    conn = get_db()
    post = conn.execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if post is None:
        conn.close()
        return "글을 찾을 수 없습니다.", 404
    if request.method == "POST":
        conn.execute("UPDATE posts SET title = ?, content = ? WHERE id = ?",
                     (request.form["title"], request.form["content"], post_id))
        conn.commit()
        conn.close()
        return redirect(url_for("post_detail", post_id=post_id))
    conn.close()
    return render_template("edit.html", post=post)


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    """글 삭제: POST로 들어오면 DB에서 해당 글을 삭제하고 목록으로 이동"""
    conn = get_db()
    conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("post_list"))


if __name__ == "__main__":
    # Render는 PORT 환경변수로 포트를 알려주고, 로컬은 5000번 사용
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
