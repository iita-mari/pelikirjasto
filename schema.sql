CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
    min_players INTEGER NOT NULL,
    max_players INTEGER NOT NULL,
    age_recommendation TEXT NOT NULL CHECK (age_recommendation IN ('5+', '6+', '7+', '8+', '9+', '10+', '12+', '13+', '14+', '17+', '18+', '21+')),
    difficulty_level TEXT NOT NULL CHECK (difficulty_level IN ('Erittäin helppo', 'Helppo', 'Keskitaso', 'Vaikea', 'Erittäin vaikea')),
    rating TEXT NOT NULL CHECK (rating IN ('*', '**', '***', '****', '*****')),
    user_id INTEGER REFERENCES users
);