import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="snake_game",
        user="postgres",
        password="postgresql"
    )

def getcreate_user(username):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id

def save_score(user_id, score, level):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    conn.commit()
    cur.close()
    conn.close()
