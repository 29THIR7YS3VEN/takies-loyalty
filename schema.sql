drop table if exists users;

CREATE TABLE users (
<<<<<<< HEAD
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  password TEXT,
  current_stamps INTEGER,
  date_joined TEXT
);
=======
  id INTEGER PRIMARY KEY AUTOINCRIMENT,
  username TEXT,
  email TEXT,
  current_stamps INTEGER,
  date_joined TEXT
);
>>>>>>> 1ad98b5242bef6c9e64bd7e1be462cc99670c356
