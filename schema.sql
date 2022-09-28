CREATE TABLE IF NOT EXISTS bookmark_list (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 bookmark_title TEXT NOT NULL,
 bookmark_url TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmark_view (
 column_id INTEGER CHECK (column_id < 5) NOT NULL UNIQUE,
 bookmark_order TEXT NOT NULL
);
