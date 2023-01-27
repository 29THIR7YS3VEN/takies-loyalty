drop table if exists users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  password TEXT,
  current_stamps INTEGER,
  date_joined TEXT
);
