from database.db_connection import DBConnection
from logs.logger_of_system import logger
from datetime import datetime

class AppointmentDB:
    def __init__(self):
        self.db = DBConnection()
    
    def create_appointment(self,data:dict):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            sql_q = """INSERT INTO appointments(patient_name, patient_email, doctor_id, appointment_date) VALUES(%s, %s, %s, %s)"""
            values = [data["patient_name"],data["patient_email"],data["doctor_id"],data["appointment_date"]]
            cursor.execute(sql_q,values)
            conn.commit()
            return True if cursor.rowcount > 0 else False
        finally:
            cursor.close()
            conn.close()
        
    def get_all_appointments(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM appointments")
            data = cursor.fetchall()
            return data
        finally:
            cursor.close()
            conn.close()

    def get_appointment_by_id(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM appointments WHERE id = %s",(id,))
            data = cursor.fetchone()
            return data
        finally:
            cursor.close()
            conn.close()


    def get_appointments_by_doctor(self,doctor_id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM appointments WHERE doctor_id = %s",(doctor_id,))
            data = cursor.fetchall()
            return data
        finally:
            cursor.close()
            conn.close()


    def complete_appointment(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE appointments SET status = 'completed' WHERE id = %s",(id,))
            conn.commit()
            return True if cursor.rowcount > 0 else False
        finally:
            cursor.close()
            conn.close()


    def cancel_appointment(self,id:int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE appointments SET status = 'cancelled' WHERE id = %s",(id,))
            conn.commit()
            return True if cursor.rowcount > 0 else False
        finally:
            cursor.close()
            conn.close()


    def count_by_status(self,status:str):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) AS count FROM appointments WHERE status = %s",(status,))
            data = cursor.fetchone()
            return data
        finally:
            cursor.close()
            conn.close()



    # def count_by_specialty(self,specialty:str):
    #     conn = self.db.get_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     try:
    #         cursor.execute("SELECT COUNT(*) AS count FROM appointments  WHERE status = 'scheduled' AND WHERE specialty = %s",(specialty,))
    #         data = cursor.fetchone()
    #         return data
    #     finally:
    #         cursor.close()
    #         conn.close()




appoint = AppointmentDB()
# appoint.create_appointment({"patient_name":"ron","patient_email":"ron@gmail.com","doctor_id":1,"appointment_date":datetime.now()})
# print(appoint.get_all_appointments())
# print(appoint.get_appointment_by_id(1))
# print(appoint.get_appointments_by_doctor(1))