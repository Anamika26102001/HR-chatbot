"""Utility functions for the RAG system."""
from typing import List
from app.models.employee import Employee
from app.core.constants import SKILLS

def create_employee_text(employee: Employee) -> str:
    """Create a searchable text representation of an employee."""
    return f"{employee.name} is a {employee.specialization} based in {employee.location} with {employee.experience_years} years of experience. " \
           f"Their skills include {', '.join(employee.skills)} and they have worked on projects like {', '.join(employee.projects)}. " \
           f"Current status: {employee.availability}"

def extract_skills_from_query(query: str) -> List[str]:
    """Extract skill requirements from query."""
    found_skills = []
    query_lower = query.lower()
    
    
    all_skills = []
    for category in SKILLS.values():
        all_skills.extend(category)
    
   
    for skill in all_skills:
        if skill in query_lower:
            found_skills.append(skill)
    
    return found_skills

def create_response_message(query: str, employees: List[Employee]) -> str:
    """Create a natural language response message."""
    if not employees:
        return "I couldn't find any employees matching your criteria."
    
    message = f"Based on your query '{query}', I found {len(employees)} relevant candidates:\n\n"
    
    for emp in employees:
        message += (f"- {emp.name} ({emp.specialization} in {emp.location})\n"
                  f"  Experience: {emp.experience_years} years\n"
                  f"  Skills: {', '.join(emp.skills)}\n"
                  f"  Notable Projects: {', '.join(emp.projects)}\n"
                  f"  Status: {emp.availability}\n\n")
    
    return message 