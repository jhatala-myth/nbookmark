##
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    config_query = "SELECT value FROM bookmark_config WHERE item = 'title';"
    get_query = "SELECT column_id, bookmark_order, column_title FROM bookmark_view ORDER BY column_id;"
    ''' DB Connect '''
    db_conn = sqlite3.connect("db/nbookmark.db")
    db_cursor = db_conn.cursor()
    try:
        db_cursor.execute(get_query)
    except sqlite3.Error as db_error:
        return render_template('error.html', error_msg=' '.join(db_error.args))

    ''' Fetch links from DB '''
    columns = []
    records = db_cursor.fetchall()
    for row in records:
        '''
            structure:
            columns = [ {"title": "column_title", "links": { "bookmark_title": "bookmark_url", ...  }} ] 
        '''
        columns.append({"title": row[2], "links": {}})
        link_query = 'SELECT bookmark_title, bookmark_url FROM bookmark_list WHERE id IN ({})'.format(','.join(row[1].split(',')))
        db_cursor.execute(link_query)
        items = db_cursor.fetchall()
        [columns[len(columns)-1]["links"].update({_[0]: _[1]}) for _ in items]

    db_cursor.execute(config_query)
    config = db_cursor.fetchall()

    return render_template('index.html', url_list=columns, title=config[0][0])


if __name__ == '__main__':
    app.run()
