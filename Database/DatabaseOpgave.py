import sqlite3

con = sqlite3.connect("school.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Students(student_id INTEGER PRIMARY KEY, name TEXT, major TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Courses(course_id INTEGER PRIMARY KEY, course_name TEXT, instructor TEXT)")

students_data = [
    (1, 'Ruben', 'Computer Science'),
    (2, 'Lars', 'Physics'),
    (3, 'Magnus', 'Biology'),
    (4, 'Anders', 'Mathematics'),
    (5, 'Sebastian', 'English')
]
cur.executemany("INSERT INTO Students(student_id, name, major) VALUES (?, ?, ?)", students_data)


courses_data = [
    (1, 'AI & Data', 'Jesper'),
    (2, 'Intro til AI', 'Lasse'),
    (3, 'DUAS', 'Andreas'),
    (4, 'Matematik', 'Morten'),
    (5, 'Brugerindragelse', 'Henrik')
]
cur.executemany(
    "INSERT INTO Courses(course_id, course_name, instructor) VALUES (?, ?, ?)", courses_data)

cur.execute("CREATE TABLE IF NOT EXISTS Enrollments(""enrollment_id INTEGER PRIMARY KEY,""student_id INTEGER,""course_id INTEGER,""FOREIGN KEY(student_id) REFERENCES Students(student_id),""FOREIGN KEY(course_id) REFERENCES Courses(course_id)"")")

enrollments_data = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (5, 1)]

cur.executemany("INSERT INTO Enrollments(student_id, course_id) VALUES (?, ?)", enrollments_data)

cur.execute("SELECT Courses.course_name FROM Courses INNER JOIN Enrollments ON Courses.course_id = Enrollments.course_id WHERE Enrollments.student_id = 1")
cur.execute("SELECT Students.name FROM Students INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id WHERE Enrollments.course_id = 2")
    
con.commit()
