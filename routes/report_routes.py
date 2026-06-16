from fastapi import APIRouter
from database.appointment_db import appoint
from database.doctor_db import doctor


router = APIRouter()


@router.get("summary")
def general_report():
    build_report = {"total_appointments": len(appoint.get_all_appointments()),
  "scheduled": appoint.count_by_status("scheduled")[0],
  "completed": appoint.count_by_status("completed")[0],
  "cancelled": appoint.count_by_status("cancelled")[0],
  "active_doctors": doctor.count_active_doctors()[0]}
    return build_report


# @router.get("/by-specialty")
# def get_appointments_by_specialty():
#     data = {"General":doctor.count_by_specialty("General"),
#             "Cardiology":appoint.count_by_specialty("Cardiology"),
#             "Dermatology" : appoint.count_by_specialty("Dermatology"),
#             "Orthopedics" : appoint.count_by_specialty("Orthopedics"),
#             "Pediatrics" : appoint.count_by_specialty("Pediatrics")
#             }
#     print(data)
#     return True

@router.get("/busiest-doctor")
def get_busiest_doctor():
    return doctor.get_busiest_doctor()
