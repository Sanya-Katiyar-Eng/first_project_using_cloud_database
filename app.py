from flask import Flask, render_template, request, redirect, flash
import psycopg
import os

app = Flask(__name__)
app.secret_key = "secret_key_for_flash"

# Cloud DB connection
url = os.environ.get("DATABASE_URL")
if not url:
    print("❌ Error: DATABASE_URL environment variable not set")
    exit()

try:
    conn = psycopg.connect(url) 
except Exception as e:
    print("❌ Could not connect to cloud DB:", e)
    exit()

# Flask route for form
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
        paid = request.form.get("paid")

        # Basic validation
        if not name or not roll or not email:
            flash("❌ Name, Roll, Email are required")
            return redirect("/")

        # Database insertion
        try:
            cur = conn.cursor()
            cur.execute("SELECT roll FROM student_registration WHERE roll = %s", (roll,))
            existing = cur.fetchone()

            if existing:
                flash(f"⚠️ Student with roll {roll} already exists")
            else:
                query = """
                INSERT INTO student_registration
                (name, roll, enrollment_num, email, course, department, pre_sem, per_sem_result, attendance, paid_seet)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
                cur.execute(query, (name, roll, enrollment_num, email, course, department, pre_sem, pre_sem_result, attendance, paid))
                conn.commit()
                flash("✅ Data inserted successfully")
            cur.close()
        except Exception as e:
            flash(f"❌ Database error: {e}")

        return redirect("/")

    return render_template("form.html")  # HTML form template

if __name__ == "__main__":
    app.run(debug=True)
