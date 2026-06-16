from fastapi import APIRouter
from database.appointment_db import appoint
from pydantic import BaseModel



router = APIRouter()

class CreateAppointment(BaseModel):
    patient_name : str
    patient_email : str
    doctor_id : int
    appointment_date : str

@router.post("",status_code=201)
def create_appointment(data:CreateAppointment):
    return appoint.create_appointment(data.model_dump())

@router.get("")
def get_all_appointments():
    return appoint.get_all_appointments()

@router.get("/{id}")
def get_appointment_by_id(id:int):
    return appoint.get_appointment_by_id(id)

@router.get("/doctor/{doctor_id}")
def get_appointments_by_doctor(doctor_id:int):
    return appoint.get_appointments_by_doctor(doctor_id)

@router.patch("/{id}/complete")
def complete_appointment(id:int):
    return appoint.complete_appointment(id)

@router.patch("/{id}/cancel")
def cancel_appointment(id:int):
    return appoint.cancel_appointment(id)

