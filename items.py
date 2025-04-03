import db

def add_item(title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id):
    sql = """INSERT INTO items (title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id])

def get_items():
    sql = "SELECT id, title FROM items ORDER BY id DESC"
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.min_players,
                    items.max_players,
                    items.age_recommendation,
                    items.difficulty_level,
                    items.rating,
                    users.id user_id,
                    users.username
             FROM items, users
             WHERE items.user_id = users.id AND
                   items.id = ?"""
    return db.query(sql, [item_id]) [0]

def update_item(item_id, title, min_players, max_players, age_recommendation, difficulty_level, rating):
    sql = """UPDATE items SET title = ?,
                              min_players = ?,
                              max_players = ?,
                              age_recommendation = ?,
                              difficulty_level = ?,
                              rating = ?
                          WHERE id = ?"""
    db.execute(sql, [title, min_players, max_players, age_recommendation, difficulty_level, rating, item_id])

def remove_item(item_id):
    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])