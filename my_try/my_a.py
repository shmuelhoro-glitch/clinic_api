# doctor_db
# -----------------------------------------

# import functools



# def with_connection(func):
#     @functools.wraps(func)
#     def wrapper(self,*args,**kwargs):
#         conn = self.db.get_connection()
#         cursor = conn.cursor(dictionary=True)
#         try:
#             result = func(self,cursor,*args,**kwargs)
#             conn.commit()
#             return result
#         finally:
#             cursor.close()
#             conn.close()
#     return wrapper




 # @with_connection
    # def create_doctor(self,cursor,data:dict):
    #     val_hold = ', '.join(["%s"]*len(data))
    #     sql_q = f"INSERT INTO doctors({', '.join(data.keys())} , is_active, max_daily_appointments) VALUES({val_hold}, TRUE, 10)"
    #     values = [val for val in data.values()]
    #     cursor.execute(sql_q,values)
    #     return True

    # def get_all_doctors(self):
    #     conn = self.db.get_connection()
    #     cursor = conn.cursor(dictionary=True)
    #     try:
    #         cursor.execute("SELECT * FROM doctors")
    #         return cursor.fetchall()
    #     finally:
    #         cursor.close()
    #         conn.close()




















