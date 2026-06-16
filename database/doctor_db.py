from database.db_connection import DBConnection,mysql
from logs.logger_of_system import logger


class DoctorDB:
    def __init__(self):
        self.db = DBConnection()
    def create_doctor(self,data:dict):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            val_hold = ', '.join(["%s"]*len(data))
            sql_q = f"INSERT INTO doctors({', '.join(data.keys())} , is_active, max_daily_appointments) VALUES({val_hold}, TRUE, 10)"
            values = [val for val in data.values()]
            print(sql_q,values)
            cursor.execute(sql_q,values)
            conn.commit()
            return True
        except mysql.connector.errors.ProgrammingError as e:
            self.db.create_tables()
            raise {f"msg":"error, please try again {e.msg}"}
        finally:
            cursor.close()
            conn.close()

    def get_all_doctors(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM doctors")
            data = cursor.fetchall()
            return data
            
        finally:
            cursor.close()
            conn.close()
    
    def get_doctor_by_id(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM doctors WHERE id = %s",(id,))
            data = cursor.fetchone()
            return data
        finally:
            cursor.close()
            conn.close()

    def update_doctor(self,id:int,data:dict):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            sql_keys = ", ".join(f"{key} = %s" for key in data) + " WHERE id = %s"
            values = list(data.values()) + [id]
            cursor.execute(f"UPDATE doctors SET {sql_keys} ",values)
            conn.commit()
            return True if cursor.rowcount > 0 else False
           
        finally:
            cursor.close()
            conn.close()

    def deactivate_doctor(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("UPDATE doctors SET is_active = FALSE WHERE id = %s",(id,))
            conn.commit()
            return True if cursor.rowcount > 0 else False
        finally:
            cursor.close()
            conn.close()


    def activate_doctor(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("UPDATE doctors SET is_active = TRUE WHERE id = %s",(id,))
            conn.commit()
            return True if cursor.rowcount > 0 else False
        finally:
            cursor.close()
            conn.close()


    def count_active_doctors(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) AS 'active doctors' FROM doctors WHERE is_active = TRUE ")
            data = cursor.fetchone()
            return data
        finally:
            cursor.close()
            conn.close()



    def get_busiest_doctor(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT d.id, d.name, COUNT(a.id) AS appointment_count FROM doctors d JOIN appointments a ON a.doctor_id = d.id WHERE a.status = 'scheduled' GROUP BY d.id ORDER BY appointment_count DESC LIMIT 1 ")
            data = cursor.fetchall()
            return data
        finally:
            cursor.close()
            conn.close()


    def count_daily_appointments(self,doctor_id,date):
        pass















doctor = DoctorDB()
# doctor.create_doctor({"name":"dan","specialty":"General"})
# print(doctor.get_all_doctors())
# print(doctor.get_doctor_by_id(1))
# print(doctor.update_doctor(1,{"name":"shmuel"}))
# print(doctor.deactivate_doctor(1))
# print(doctor.get_doctor_by_id(1))
# print(doctor.count_active_doctors())
# print(doctor.get_busiest_doctor())