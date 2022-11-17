##
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def sql_query(cursor, query):
    try:
        _result = cursor.execute(query)
    except sqlite3.Error as db_error:
        return {"status": False, "data": db_error.args}
    return {"status": True, "data": _result.fetchall()}


@app.route('/')
def index():
    site_data = {}
    config_query = "SELECT value FROM bookmark_config WHERE item = 'title';"
    get_query = "SELECT bookmark_view.tab_id AS tab_index, tab_title, column_id, column_title, bookmark_order " \
                "FROM bookmark_view LEFT JOIN bookmark_tab ON (bookmark_tab.tab_id=bookmark_view.tab_id)" \
                "ORDER BY tab_index, column_id;"
    col_query = "SELECT bookmark_title, bookmark_url FROM bookmark_list WHERE id IN ({})"

    ''' DB Connect '''
    db_conn = sqlite3.connect("db/nbookmark.db")
    db_conn.row_factory = sqlite3.Row
    db_cursor = db_conn.cursor()

    result = sql_query(db_cursor, config_query)
    if not result['status']:
        return render_template('error.html', error_msg=' '.join(result['data']))

    site_data['title'] = result['data'][0]['value']

    ''' Fetch links from DB '''
    tabs = []

    result = sql_query(db_cursor, get_query)
    if not result['status']:
        return render_template('error.html', error_msg=' '.join(result['data']))
    tab_index_list = {}
    for row in result['data']:
        if row['tab_index'] not in tab_index_list.keys():
            tab_index_list[row['tab_index']] = len(tab_index_list)
            tabs.append({'tab_id': row['tab_index'], 'tab_title': row['tab_title'], 'columns': []})

        tab_index = tab_index_list[row['tab_index']]
        tabs[tab_index]['columns'].append({"title": row['column_title'], "links": {}})

        columns = sql_query(db_cursor, col_query.format(','.join(row['bookmark_order'].split(','))))
        if not columns['status']:
            return render_template('error.html', error_msg=' '.join(columns['data']))

        for col in columns['data']:
            col_index = len(tabs[tab_index]['columns']) - 1
            '''
                structure:
                columns = [ {"title": "column_title", "links": { "bookmark_title": "bookmark_url", ...  }} ] 
            '''
            tabs[tab_index]['columns'][col_index]['links'].update({col['bookmark_title']: col['bookmark_url']})

    site_data['tabs'] = tabs
    return render_template('index.html', data=site_data)


if __name__ == '__main__':
    app.run()
