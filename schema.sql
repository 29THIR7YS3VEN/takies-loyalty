drop table if exists users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCRIMENT,
  username TEXT,
  email TEXT,
  current_stamps INTEGER,
  date_joined TEXT
);
