import db

def add_item(title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id):
    sql = """INSERT INTO items (title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, min_players, max_players, age_recommendation, difficulty_level, rating, user_id])