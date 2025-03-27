from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",       
        password="kunaldubeysql@10", 
        database="bus_planner",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/search', methods=['POST'])
def search_route():
    data = request.json
    start_location = data.get("start_location")
    end_location = data.get("end_location")

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT * FROM routes WHERE start_location = %s AND end_location = %s
    """
    cursor.execute(query, (start_location, end_location))
    results = cursor.fetchall()
    conn.close()

    if results:
        return jsonify({"routes": results})
    else:
        return jsonify({"routes": "No route found."})

if __name__ == '__main__':
    app.run(debug=True)
