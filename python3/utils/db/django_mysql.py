from django.db import connection


def query(sql, list1=()):
    cursor = connection.cursor()
    if not list1:
        cursor.execute(sql)
    else:
        cursor.execute(sql, list1)
    result = cursor.fetchall()

    connection.commit()
    connection.close()
    return result


def query_one(sql, list1=()):
    cursor = connection.cursor()
    if not list1:
        cursor.execute(sql)
    else:
        cursor.execute(sql, list1)
    result = cursor.fetchone()

    connection.commit()
    connection.close()
    return result


def save(sql, list1=()):
    cursor = connection.cursor()
    try:
        if not list1:
            result = cursor.execute(sql)
        else:
            result = cursor.execute(sql, list1)
        connection.commit()
        return result
    except Exception as e:
        print (e)
        connection.rollback()
        return None
    connection.close()