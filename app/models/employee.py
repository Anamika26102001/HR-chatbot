from typing import List, Optional
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    skills: List[str]
    experience_years: int
    projects: List[str]
    availability: str
    specialization: str
    location: str

class EmployeeQuery(BaseModel):
    query: str

class EmployeeResponse(BaseModel):
    message: str
    employees: Optional[List[Employee]] = None 