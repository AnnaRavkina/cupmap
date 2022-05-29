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

def get_users(user_id):
    return query('SELECT * FROM Users WHERE UserId = ?', user_id)

def get_locations(location_id):
    return query("""
        SELECT * FROM Locations 
        INNER JOIN Comments
	        ON Locations.Id = Comments.LocationId
        INNER JOIN Users
	        ON Comments.UserId = Users.UserId
        INNER JOIN (SELECT CommentId, COUNT(UserId) AS LikeCount FROM Likes GROUP BY CommentId) L
	        ON Comments.CommentId = L.CommentId
        WHERE Locations.Id = ?
    """, location_id)

def get_comments(comment_id):
    return query("""
        SELECT * FROM Comments
        INNER JOIN Users
            ON Comments.UserId = Users.UserId
        INNER JOIN Locations
            ON Comments.LocationId = Locations.Id
        INNER JOIN (SELECT CommentId, COUNT(UserId) AS LikeCount FROM Likes GROUP BY CommentId) L
            ON Comments.CommentId = L.CommentId
        WHERE Comments.CommentId = ?
    """, comment_id)