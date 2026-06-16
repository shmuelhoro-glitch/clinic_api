import mysql.connector


class DBConnection:
    def get_connection(self):
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "clinic_db"
        )
    

    def create_tables(self):
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root"
        )
        cursor = conn.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS clinic_db")
            cursor.execute("USE clinic_db")
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS doctors(
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           name VARCHAR(50) NOT NULL,
                           specialty ENUM("General", "Cardiology", "Dermatology", "Orthopedics", "Pediatrics") NOT NULL,
                           is_active BOOLEAN NOT NULL,
                           max_daily_appointments INT NOT NULL DEFAULT 10
                            )""")
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS appointments(
                           id INT AUTO_INCREMENT PRIMARY KEY,
                           patient_name VARCHAR(50) NOT NULL,
                           patient_email VARCHAR(100) UNIQUE NOT NULL,
                           doctor_id INT NOT NULL,
                           appointment_date DATE NOT NULL,
                           status ENUM("cancelled", "completed", "scheduled") NOT NULL DEFAULT "scheduled" ,
                           FOREIGN KEY (doctor_id) REFERENCES doctors(id),
                           UNIQUE (patient_email, doctor_id, appointment_date)
                            )""")
            conn.commit()
            return True
        finally:
            cursor.close()
            conn.close()
        
        


