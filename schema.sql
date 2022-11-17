CREATE TABLE IF NOT EXISTS bookmark_list (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 bookmark_title TEXT NOT NULL,
 bookmark_url TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmark_tab (
 tab_id INTEGER PRIMARY KEY AUTOINCREMENT,
 tab_title TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmark_view (
 tab_id INTEGER NOT NULL,
 column_id INTEGER CHECK (column_id < 4) NOT NULL,
 column_title TEXT NOT NULL,
 bookmark_order TEXT NOT NULL,
 FOREIGN KEY (tab_id) REFERENCES bookmark_tab(tab_id),
 UNIQUE (tab_id, column_id)
);

CREATE TABLE IF NOT EXISTS bookmark_config (
 item TEXT NOT NULL UNIQUE,
 value TEXT NOT NULL
);

