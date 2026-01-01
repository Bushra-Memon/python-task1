import sqlite3
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("select * from user where id = ?",(user_id,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return "Error: User Not Found!"

    cursor.execute("delete from user where id = ?",(user_id,))
    conn.commit()
    conn.close()

    return "User Deleted Successfully"
print(delete_user(11))

