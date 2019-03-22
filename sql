CREATE TABLE IF NOT EXISTS books
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100),
        content VARCHAR(1000),
        link VARCHAR(1000)
        user_id INTEGER
    )


CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(100),
        password_hash VARCHAR(128)
    )
