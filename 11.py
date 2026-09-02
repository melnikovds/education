

def login(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users "
                   f"WHERE username = '{username}'"
                   f"AND password = '{password}'")
    result = cursor.fetchone()
    conn.close()
    return result