import random
import sqlite3

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM items")
db.execute("DELETE FROM comments")
db.execute("DELETE FROM item_classes")

user_count = 1000
item_count = 10**5
comment_count = 10**6

for i in range(1, user_count + 1):
    db.execute("INSERT INTO users (username, password_hash, image) VALUES (?, ?, ?)",
               ["user" + str(i), "password_hash" + str(i), None])

for i in range(1, item_count + 1):
    db.execute("INSERT INTO items (title, min_players, max_players, age_recommendation, duration, difficulty_level, rating, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               ["item" + str(i), random.randint(1, 4), random.randint(5, 10), "10+", "1h", "easy", "5", random.randint(1, user_count)])

for i in range(1, comment_count + 1):
    user_id = random.randint(1, user_count)
    item_id = random.randint(1, item_count)
    db.execute("INSERT INTO comments (comment_text, user_id, item_id) VALUES (?, ?, ?)",
               ["comment" + str(i), user_id, item_id])

db.commit()
db.close()