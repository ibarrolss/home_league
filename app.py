from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, static_folder='C:/Users/sebastian.ibarrola/Desktop/mateo/webs/try/static/logos')

@app.route('/')
def league_table():
    cnx = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0612sebaynuria',
        database='home_league'
    )

    cursor = cnx.cursor()
    cursor.execute('SELECT * FROM LeagueTable ORDER BY Pts DESC, GT DESC')
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()

    return render_template('league_table.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
