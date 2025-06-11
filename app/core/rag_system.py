import json
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models.employee import Employee

class RAGSystem:
    def __init__(self):
        # Initialize the sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.employees: List[Employee] = []
        self.employee_embeddings = None
        self.load_employees()

    def load_employees(self):
        """Load employees from JSON file and create embeddings"""
        try:
            with open('data/employees.json', 'r') as f:
                data = json.load(f)
                self.employees = [Employee(**emp) for emp in data['employees']]
                
            # Create embeddings for each employee
            employee_texts = [self._create_employee_text(emp) for emp in self.employees]
            self.employee_embeddings = self.model.encode(employee_texts)
        except Exception as e:
            print(f"Error loading employees: {str(e)}")
            self.employees = []
            self.employee_embeddings = None

    def _create_employee_text(self, employee: Employee) -> str:
        """Create a searchable text representation of an employee"""
        return f"{employee.name} is a {employee.specialization} based in {employee.location} with {employee.experience_years} years of experience. " \
               f"Their skills include {', '.join(employee.skills)} and they have worked on projects like {', '.join(employee.projects)}. " \
               f"Current status: {employee.availability}"

    def process_query(self, query: str) -> Dict:
        """Process a natural language query and return relevant employees"""
        try:
            # Encode the query
            query_embedding = self.model.encode([query])
            
            # Calculate similarity scores
            similarities = cosine_similarity(query_embedding, self.employee_embeddings)[0]
            
            # Get top matches
            top_indices = np.argsort(similarities)[::-1][:3]  # Get top 3 matches
            
            relevant_employees = [self.employees[i] for i in top_indices if similarities[i] > 0.1]
            
            if not relevant_employees:
                return {
                    "message": "No matching employees found for your query.",
                    "employees": []
                }
            
            # Create response message
            response_message = self._create_response_message(query, relevant_employees)
            
            return {
                "message": response_message,
                "employees": relevant_employees
            }
            
        except Exception as e:
            return {
                "message": f"Error processing query: {str(e)}",
                "employees": []
            }

    def _create_response_message(self, query: str, employees: List[Employee]) -> str:
        """Create a natural language response message"""
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