import sqlite3
def update_user(user_id, new_name=None, new_email=None):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("select * from user where id = ?",(user_id,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return "Error: User Not Found!"

    if new_name:
        cursor.execute("update user set name = ? where id = ?",(new_name,user_id))

    if new_email:
        cursor.execute("update user set email = ? where id = ?",(new_email,user_id))

    conn.commit()
    conn.close()
    return "User Updated Successfully!!!"

print(update_user(1, new_email = 'bushramemon192@gmail.com'))
print(update_user(8, new_name = 'Moinuddin'))