##
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    get_query = "SELECT column_id, bookmark_order FROM bookmark_view ORDER BY column_id;"
    db_conn = sqlite3.connect("db/nbookmark.db")
    db_cursor = db_conn.cursor()
    try:
        db_cursor.execute(get_query)
    except sqlite3.Error as db_error:
        return render_template('error.html', error_msg=' '.join(db_error.args))
    columns = {}
    records = db_cursor.fetchall()
    for row in records:
        columns[row[0]] = {}
        link_query = 'SELECT bookmark_title, bookmark_url FROM bookmark_list WHERE id IN ({})'.format(','.join(row[1].split(',')))
        db_cursor.execute(link_query)
        items = db_cursor.fetchall()
        [columns[row[0]].update({_[0]: _[1]}) for _ in items]

    return render_template('index.html', url_list=columns, title="Bookmarks")


if __name__ == '__main__':
    app.run()
