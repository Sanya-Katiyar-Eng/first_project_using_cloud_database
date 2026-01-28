# 🎓 Student Registration Web Application

This project is a Student Registration Web Application built using **Flask (Python)** and **PostgreSQL**.  
It allows users to enter student details through a web form and saves the data securely in a database.

This project is created for learning and practice purposes and demonstrates the use of Flask, HTML, CSS, and PostgreSQL with environment variables.

---

## 📌 Project Description

The Student Registration Web Application provides a simple and interactive interface where students can fill in their personal and academic details such as:

- Name  
- Roll Number  
- Enrollment Number  
- Email  
- Course  
- Department  
- Previous Semester  
- Previous Semester Result  
- Attendance  

All submitted data is stored in a PostgreSQL database.  
The application also checks for duplicate roll numbers and shows success or error messages using Flask flash messages.

---

## 🚀 Features

- User-friendly student registration form  
- Data stored in PostgreSQL database  
- Duplicate roll number validation  
- Flash messages for success and error  
- Environment variables for security (`SECRET_KEY`, `DATABASE_URL`)  
- Clean and simple UI design  
- Ready for deployment on cloud platforms  

---

## 🗂 Project Structure

cloud_project/
│
├── app.py
├── requirements.txt
├── Procfile
├── .env
│
├── templates/
│ └── form.html


---

## ⚙️ Technologies Used

- Python  
- Flask  
- PostgreSQL  
- HTML  
- CSS  
- Git & GitHub  
- python-dotenv  
- Gunicorn  

---

## 🔐 Environment Variables

Create a `.env` file in the project root and add the following:


These variables help keep sensitive information secure and are not uploaded to GitHub.

---

## ▶️ How to Run the Project Locally

1. Clone the repository:

https://github.com/Sanya-Katiyar-Eng/first_project_using_cloud_database



2. Go to the project folder:


3. Install required packages:

4. Create a `.env` file and add environment variables.

5. Run the application:
6. Open your browser and go to:


---

## 🗄 Database Setup

Create the following table in PostgreSQL:

```sql
CREATE TABLE student_registration (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll VARCHAR(50) UNIQUE NOT NULL,
    enrollment_num VARCHAR(50),
    email VARCHAR(100) NOT NULL,
    course VARCHAR(50),
    department VARCHAR(50),
    pre_sem VARCHAR(20),
    pre_sem_result VARCHAR(20),
    attendance VARCHAR(20)
);


👨‍💻 Author     : sanya katiyar