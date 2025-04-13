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
    duration TEXT NOT NULL CHECK (duration IN ('15 min', '30 min', '45 min', '1 tunti', '1,5 tuntia', '2 tuntia', 'enemmän')),
    difficulty_level TEXT NOT NULL CHECK (difficulty_level IN ('Erittäin helppo', 'Helppo', 'Keskitaso', 'Vaikea', 'Erittäin vaikea')),
    rating TEXT NOT NULL CHECK (rating IN ('*', '**', '***', '****', '*****')),
    user_id INTEGER REFERENCES users
);

CREATE TABLE item_classes (
    id INTEGER PRIMARY KEY,
    item_id INTEGER REFERENCES items,
    title TEXT,
    value TEXT
);