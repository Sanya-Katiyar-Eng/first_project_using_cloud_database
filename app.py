from flask import Flask, render_template, request, redirect, flash
import psycopg
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "default_dev_secret_key")

# Get DATABASE_URL from Railway
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise Exception("DATABASE_URL is not set")

# Connect to DB
def get_db_connection():
    return psycopg.connect(DATABASE_URL, connect_timeout=100)

@app.route("/", methods=["GET", "POST"])
def student_form():
    if request.method == "POST":
        name = request.form.get("name")
        roll = request.form.get("roll")
        enrollment_num = request.form.get("enrollment_num")
        email = request.form.get("email")
        course = request.form.get("course")
        department = request.form.get("department")
        pre_sem = request.form.get("pre_sem")
        pre_sem_result = request.form.get("pre_sem_result")
        attendance = request.form.get("attendance")

        if not name or not roll or not email:
            flash("Name, Roll and Email are required")
            return redirect("/")

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:

                    # Check existing roll
                    cur.execute(
                        "SELECT roll FROM student_registration WHERE roll = %s",
                        (roll,)
                    )
                    existing = cur.fetchone()

                    if existing:
                        flash(f"Student with roll {roll} already exists")
                    else:
                        query = """
                        INSERT INTO student_registration
                        (name, roll, enrollment_num, email, course, department, pre_sem, pre_sem_result, attendance)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """
                        cur.execute(query, (
                            name, roll, enrollment_num, email,
                            course, department, pre_sem, pre_sem_result,
                            attendance
                        ))
                        conn.commit()
                        flash("Data inserted successfully")

        except Exception as e:
            flash(f"Database error: {e}")

        return redirect("/")

    return render_template("form.html", active_page="form")


if __name__ == "__main__":
    app.run(debug=True)
