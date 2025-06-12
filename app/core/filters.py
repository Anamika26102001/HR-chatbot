"""Filter functionality for the RAG system."""
from typing import List, Tuple, Optional
import re
from app.models.employee import Employee
from app.core.constants import EXPERIENCE_PATTERNS

class QueryFilters:
    @staticmethod
    def extract_experience_filter(query: str) -> Tuple[Optional[int], Optional[str]]:
        """Extract experience filter from query."""
        query_lower = query.lower()
        
        
        for pattern in EXPERIENCE_PATTERNS['greater_than']:
            match = re.search(pattern, query_lower)
            if match:
                return int(match.group(1)), '>='
        
        
        for pattern in EXPERIENCE_PATTERNS['less_than']:
            match = re.search(pattern, query_lower)
            if match:
                return int(match.group(1)), '<'
        
        return None, None

    @staticmethod
    def filter_by_experience(employees: List[Employee], years: int, operator: str) -> List[Employee]:
        """Filter employees by experience."""
        if operator == '>=':
            return [emp for emp in employees if emp.experience_years >= years]
        elif operator == '<':
            return [emp for emp in employees if emp.experience_years < years]
        return employees

    @staticmethod
    def filter_by_skills(employees: List[Employee], required_skills: List[str]) -> List[Employee]:
        """Filter employees by required skills."""
        if not required_skills:
            return employees
            
        filtered_employees = []
        for emp in employees:
            emp_skills = [skill.lower() for skill in emp.skills]
            if all(skill.lower() in emp_skills for skill in required_skills):
                filtered_employees.append(emp)
        
        return filtered_employees 