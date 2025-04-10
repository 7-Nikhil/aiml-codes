import mysql.connector as mysql

def connection() -> mysql.MySQLConnection:
    return mysql.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="college_management_system"
    )

def create_student(student) -> None:
    conn = connection()
    cursor = conn.cursor()
    query = "INSERT INTO STUDENTS(ENROLLMENT_ID, FULL_NAME, BRANCH_NAME, YEAR_OF_ADMISSION, SEMESTER) VALUES (%s, %s, %s, %s, %s)"
    values = (student.roll_no, student.name, student.branch, student.year_of_admission, student.semester)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    
print("Database connected successfully.")