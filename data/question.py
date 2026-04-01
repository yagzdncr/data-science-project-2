import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('SELECT age FROM students WHERE age > 22 ;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM courses WHERE category ='Veritabanı'""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM students WHERE first_name ILIKE 'a%';''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM courses WHERE course_name LIKE '%SQL%';''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM students WHERE age BETWEEN 22 AND 24 ;
''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT s.first_name, s.last_name FROM students s JOIN enrollments e ON s.student_id = e.student_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(''' SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, i.name
FROM courses c
JOIN instructors i ON c.course_id = i.instructor_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, COUNT(e.student_id) AS student_count
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.course_id
WHERE c.category = 'SQL'
GROUP BY c.course_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name, AVG(s.age) AS avg_age
FROM courses c
JOIN enrollments e ON e.course_id = c.course_id
JOIN students s ON s.student_id = e.student_id
GROUP BY c.course_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(''' SELECT s.first_name, s.last_name,  COUNT(e.course_id) AS total_courses
FROM students s LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT i.name AS instructor_name, 
COUNT(ci.course_id) AS total_courses
FROM instructors i
JOIN course_instructors ci ON i.instructor_id = ci.instructor_id
GROUP BY i.instructor_id, i.name
HAVING COUNT(ci.course_id) > 1;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT c.course_name , COUNT(DISTINCT student_id) AS uniq_students FROM
courses c LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT s.first_name, s.last_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name IN ('SQL Temelleri', 'İleri SQL')
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(DISTINCT c.course_id) = 2;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''SELECT 
    s.first_name, 
    s.last_name, 
    c.course_name, 
    i.name AS instructor_name, 
    e.enrollment_date
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN course_instructors ci ON c.course_id = ci.course_id
JOIN instructors i ON ci.instructor_id = i.instructor_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data