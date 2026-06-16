from fastapi import APIRouter,HTTPException
from database.doctor_db import doctor
from logs.logger_of_system import logger
from pydantic import BaseModel
from enum import Enum

router = APIRouter()




class Specialty(str,Enum):
    GENERAL = "General"
    CARDIOLOGY = "Cardiology"
    DERMATOLOGY = "Dermatology"
    ORTHOPEDICS = "Orthopedics"
    PEDIATRICS = "Pediatrics"


class CreateDoctor(BaseModel):
    name : str
    specialty : Specialty


class UpdateDoctor(BaseModel):
    name : str | None = None
    specialty : Specialty | None = None
    max_daily_appointments : int | None = None



@router.post("",status_code=201)
def create_doctor(data:CreateDoctor):
    logger.info("A call was made to add a new doctor.")
    try:
        for_return = doctor.create_doctor(data.model_dump())
        if for_return:
            logger.info("The doctor was added successfully.")
            return "The doctor was added successfully."

    except Exception as e:
        logger.warning(f"An error occurred while adding a new doctor. {e.msg}")
        raise HTTPException(500,"oops")




@router.get("")
def get_all_doctors():
    return doctor.get_all_doctors()


@router.get("/{id}")
def get_doctor_by_id(id:int):
    return doctor.get_doctor_by_id(id)

@router.patch("/{id}")
def update_doctor(id:int,data:UpdateDoctor):
    update_data = data.model_dump(exclude_none=True)
    if update_data:
        updated = doctor.update_doctor(id,update_data)
        if updated:
            return "Updated successfully✅🎉"
        else:
            raise HTTPException(400,"The information you provided is the information that was already there.🫤")
    else:
        return "I did not receive any update data.🤦‍♂️"


@router.patch("/{id}/deactivate")
def deactivate_doctor(id:int):
    return doctor.deactivate_doctor(id)




@router.patch("/{id}/activate")
def activate_doctor(id:int):
    return doctor.activate_doctor(id)














