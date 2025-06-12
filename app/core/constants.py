"""Constants used across the RAG system."""


SKILLS = {
    'languages': [
        'python', 'java', 'javascript', 'typescript'
    ],
    'frameworks': [
        'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'spring', 'express'
    ],
    'databases': [
        'mongodb', 'postgresql', 'mysql'
    ],
    'cloud': [
        'aws', 'azure', 'gcp'
    ],
    'devops': [
        'docker', 'kubernetes', 'devops'
    ],
    'specializations': [
        'machine learning', 'ai', 'data science', 'full stack', 'frontend',
        'backend', 'mobile', 'ios', 'android', 'react native', 'flutter'
    ]
}


EXPERIENCE_PATTERNS = {
    'greater_than': [
        r'(\d+)\+?\s*years?',
        r'more than (\d+)\s*years?',
        r'at least (\d+)\s*years?',
        r'minimum (\d+)\s*years?'
    ],
    'less_than': [
        r'less than (\d+)\s*years?',
        r'under (\d+)\s*years?',
        r'below (\d+)\s*years?'
    ]
}


MODEL_NAME = 'all-MiniLM-L6-v2'
SIMILARITY_THRESHOLD = 0.1
TOP_K_RESULTS = 10 