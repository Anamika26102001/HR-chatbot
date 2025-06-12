"""RAG (Retrieval-Augmented Generation) system for employee search."""
import json
from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from app.models.employee import Employee
from app.core.constants import MODEL_NAME, SIMILARITY_THRESHOLD, TOP_K_RESULTS
from app.core.filters import QueryFilters
from app.core.utils import create_employee_text, extract_skills_from_query, create_response_message

class RAGSystem:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.employees: List[Employee] = []
        self.employee_embeddings = None
        self.load_employees()

    def load_employees(self):
        """Load employees from JSON file and create embeddings."""
        try:
            with open('data/employees.json', 'r') as f:
                data = json.load(f)
                self.employees = [Employee(**emp) for emp in data['employees']]
            
            employee_texts = [create_employee_text(emp) for emp in self.employees]
            self.employee_embeddings = self.model.encode(employee_texts)
        except Exception as e:
            print(f"Error loading employees: {str(e)}")
            self.employees = []
            self.employee_embeddings = None

    def process_query(self, query: str) -> Dict:
        """Process a natural language query and return relevant employees."""
        try:
            
            exp_years, exp_operator = QueryFilters.extract_experience_filter(query)
            required_skills = extract_skills_from_query(query)
            
            
            query_embedding = self.model.encode([query])
            
            
            similarities = cosine_similarity(query_embedding, self.employee_embeddings)[0]
            
           
            top_indices = np.argsort(similarities)[::-1][:TOP_K_RESULTS]
            
            
            relevant_employees = [self.employees[i] for i in top_indices if similarities[i] > SIMILARITY_THRESHOLD]
            
          
            if exp_years is not None:
                relevant_employees = QueryFilters.filter_by_experience(relevant_employees, exp_years, exp_operator)
            
           
            if required_skills:
                relevant_employees = QueryFilters.filter_by_skills(relevant_employees, required_skills)
            
            if not relevant_employees:
                return {
                    "message": "No matching employees found for your query.",
                    "employees": []
                }
            
            response_message = create_response_message(query, relevant_employees)
            
            return {
                "message": response_message,
                "employees": relevant_employees
            }
            
        except Exception as e:
            return {
                "message": f"Error processing query: {str(e)}",
                "employees": []
            } 