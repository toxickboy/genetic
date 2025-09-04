from fastapi import FastAPI, Query,Path
from pydantic import BaseModel
from typing import Optional, List


class GeneticInfo(BaseModel):
    SNP_rs1234: Optional[int] = None
    SNP_rs5678:Optional[int]=None
    Gene_description: Optional[str] = None 
class DemoGraphics(BaseModel):
    age: Optional[int] = None
    sex: Optional[str] = None
    ethnicity: Optional[str] = None
class FamilyHistory(BaseModel):
    diabetes: Optional[bool] = None
    heart_disease: Optional[bool] = None
    cancer: Optional[bool] = None
    hypertension: Optional[bool] = None
class Lifestyle(BaseModel):
    smoking_status: Optional[str] = None
    alcohol_consumption: Optional[str] = None
    physical_activity_level: Optional[str] = None
class MedicalRecord(BaseModel):
    BMI: Optional[float] = None
    blood_pressure: Optional[float] = None
    cholesterol_level: Optional[float] = None
    blood_pressure_systolic: Optional[float] = None

class UserInfo(BaseModel):
    genetic_info:GeneticInfo
    demographics:DemoGraphics
    family_history:FamilyHistory    
    lifestyle:Lifestyle
    medical_record:MedicalRecord
    
app=FastAPI()
@app.post("/submit_user_info/")
async def submit_user_info(user_info: UserInfo):

    return {"message": "User information received successfully", "data": user_info}