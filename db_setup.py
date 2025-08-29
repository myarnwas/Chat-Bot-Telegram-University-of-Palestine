import sqlite3

conn = sqlite3.connect('notifications.db')
cursor = conn.cursor()

# جدول الطلاب كما كان
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    registration_alert INTEGER DEFAULT 0,
    exam_alert INTEGER DEFAULT 0,
    fees_alert INTEGER DEFAULT 0
)
''')

# جدول الأحداث مع وقت التنبيه لكل حدث
cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    event_type TEXT,
    event_date TEXT,
    alert_time TEXT,  -- الوقت الذي يريد فيه الطالب استلام التنبيه
    notified INTEGER DEFAULT 0,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
''')

conn.commit()
conn.close()
print("Database setup completed with alert_time column.")
