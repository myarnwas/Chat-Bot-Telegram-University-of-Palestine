import sqlite3
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import telebot



def init_db():
    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()
    
    # جدول الطلاب
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            registration_alert INTEGER DEFAULT 0,
            exam_alert INTEGER DEFAULT 0,
            fees_alert INTEGER DEFAULT 0
        )
    ''')

    # جدول الأحداث
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            event_type TEXT,
            event_date TEXT,
            alert_time TEXT,
            notified INTEGER DEFAULT 0,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# استدعاء الدالة عند بدء البوت
init_db()

# --- الدوال الأساسية ---
def add_student(student_id, registration=0, exam=0, fees=0):
    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO students(student_id, registration_alert, exam_alert, fees_alert)
        VALUES (?, ?, ?, ?)
    ''', (student_id, registration, exam, fees))
    conn.commit()
    conn.close()

def add_event(student_id, event_type, event_date, alert_time):
    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events(student_id, event_type, event_date, alert_time)
        VALUES (?, ?, ?, ?)
    ''', (student_id, event_type, event_date, alert_time))
    conn.commit()
    conn.close()

def send_notifications(bot):
    now = datetime.datetime.now()
    current_date = now.date().strftime('%Y-%m-%d')
    current_time = now.time().strftime('%H:%M')

    conn = sqlite3.connect('notifications.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT e.id, e.student_id, e.event_type, e.alert_time
        FROM events e
        JOIN students s ON e.student_id = s.student_id
        WHERE e.event_date = ? AND e.notified = 0
    ''', (current_date,))

    events = cursor.fetchall()
    for event in events:
        event_id, student_id, event_type, alert_time_str = event
        if current_time == alert_time_str:
            cursor.execute('SELECT registration_alert, exam_alert, fees_alert FROM students WHERE student_id=?', (student_id,))
            alerts = cursor.fetchone()
            registration_alert, exam_alert, fees_alert = alerts

            send = False
            if event_type == 'Registration' and registration_alert:
                send = True
            elif event_type == 'Exam' and exam_alert:
                send = True
            elif event_type == 'Fees' and fees_alert:
                send = True

            if send:
                bot.send_message(student_id, f"تذكير: {event_type} اليوم!")
                cursor.execute('UPDATE events SET notified=1 WHERE id=?', (event_id,))

    conn.commit()
    conn.close()

# --- دالة لتشغيل كل شيء (start + scheduler) ---
def start_notifications(bot, message):
    # تشغيل Scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: send_notifications(bot), 'interval', minutes=1)
    scheduler.start()

    # بدء واجهة اختيار التنبيهات مع الطالب
    student_id = message.from_user.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
    markup.add('✔️ تسجيل', '✔️ امتحانات', '✔️ رسوم', '✔️ كلهم')
    msg = bot.send_message(student_id, "اختر التنبيهات التي تريد استلامها:", reply_markup=markup)
    bot.register_next_step_handler(msg, ask_alert_time, bot, student_id)

def ask_alert_time(message, bot, student_id):
    text = message.text
    reg = exam = fees = 0
    if 'تسجيل' in text or 'كلهم' in text: reg = 1
    if 'امتحانات' in text or 'كلهم' in text: exam = 1
    if 'رسوم' in text or 'كلهم' in text: fees = 1
    add_student(student_id, reg, exam, fees)

    msg2 = bot.send_message(student_id, "أرسل وقت التنبيه بصيغة HH:MM (مثال: 09:00):")
    bot.register_next_step_handler(msg2, save_alert_time, bot, student_id, reg, exam, fees)

def save_alert_time(message, bot, student_id, reg, exam, fees):
    alert_time = message.text.strip()
    today = datetime.date.today().strftime('%Y-%m-%d')
    if reg: add_event(student_id, 'Registration', today, alert_time)
    if exam: add_event(student_id, 'Exam', today, alert_time)
    if fees: add_event(student_id, 'Fees', today, alert_time)
    bot.send_message(student_id, "تم حفظ اختياراتك مع وقت التنبيه ✅")
