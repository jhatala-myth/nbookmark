CREATE TABLE IF NOT EXISTS bookmark_list (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 bookmark_title TEXT NOT NULL,
 bookmark_url TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmark_tab (
 tab_id INTEGER PRIMARY KEY AUTOINCREMENT,
 tab_title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bookmark_view (
 column_id INTEGER CHECK (column_id < 4) NOT NULL,
 column_title TEXT NOT NULL,
 tab_id INTEGER NOT NULL,
 bookmark_order TEXT NOT NULL,
 FOREIGN KEY (tab_id) REFERENCES bookmark_tab(tab_id)
);

CREATE TABLE IF NOT EXISTS bookmark_config (
 item TEXT NOT NULL UNIQUE,
 value TEXT NOT NULL
);

INSERT INTO bookmark_tab (tab_title) VALUES ('Tab #1');
INSERT INTO bookmark_list (bookmark_title, bookmark_url) VALUES ('Bookmark #1', 'https://github.com');
INSERT INTO bookmark_view VALUES (1, 'Column #1', 1, '1');
INSERT INTO bookmark_config VALUES ('title', 'nBookmark');