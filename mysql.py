from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root1'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lineaTelefonica'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

CORS(app)


@app.route('/api/', methods=['GET'])
def get_all_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    rv = cur.fetchall()
    return jsonify(rv)


@app.route('/api/', methods=['POST'])
def add_task():
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    cur.execute("INSERT INTO tasks (title) VALUES ('" + str(title) + "')")
    mysql.connection.commit()
    result = {'title': title}
    return jsonify({'result': result})


@app.route('/api//<>', methods=['PUT'])
def update_task():
    cur = mysql.connection.cursor()
    title = request.get_json()['title']
    cur.execute("UPDATE tasks SET title = '" + str(title) + "' WHERE id = " +
                id)
    mysql.connection.commit()
    result = {'title': title}

    return jsonify({'result': result})


@app.route('/api//<>', methods=['DELETE'])
def delete_task():
    cur = mysql.connection.cursor()
    response = cur.execute("DELETE FROM tasks where id = " + id)
    mysql.connection.commit()

    if response > 0:
        result = {'message': 'record delete'}
    else:
        result = {'message': 'no record found'}

    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)