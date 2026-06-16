from fastapi import FastAPI
from routes.doctor_routes import router as doctor_routes
from routes.appointment_routes import router as appointments_routes
from routes.report_routes import router as report_routes


app = FastAPI()

app.include_router(doctor_routes,prefix="/doctors",tags=["doctors"])

app.include_router(appointments_routes,prefix="/appointments",tags=["appointments"])

app.include_router(report_routes,prefix="/reports",tags=["reports"])

