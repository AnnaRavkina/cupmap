import sqlite3, database

def query(query_text, *param):
    conn = sqlite3.connect('cupmap.db')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    rows = cur.fetchall()
    dicts = []

    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)

    conn.close()
    return dicts

def get_users():
    return query('SELECT * FROM Users')

def get_locations():
    return query('SELECT * FROM Locations')

def get_comments():
    return query("""
        SELECT
            Comments.Id,
            Comments.UserId,
            Comments.CommentText,
            Users.Name,
            Users.Username,
            Users.Picture
        FROM Comments
        INNER JOIN Users
            ON Comments.UserId = Users.Id
    """)