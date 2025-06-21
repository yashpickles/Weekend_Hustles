import json
import os
from difflib import SequenceMatcher
# Memory Manager to save important bits of information for a callback in the later in the chat 
class MemoryManager: # (patch == v1.7)
    def __init__(self):
        self.memory_file = 'memory/memory.json'
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file) and os.path.getsize(self.memory_file) > 0:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return []
        
    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=4)

    def is_similar(self, q1, q2, threshold=0.85):
        return SequenceMatcher(None, q1.lower(), q2.lower()).ratio() >= threshold

    def add_intersection(self, question, answer, tools_used=[]):
        for entry in self.memory:
            if self.is_similar(entry['question'], question):
                # Question Already exists, don't add again
                return
        entry = {
            "question": question,
            "answer": answer,
            "tools_used": tools_used
        }
        self.memory.append(entry)
        self.save_memory()
    
    def search_memory(self, query):
        query = query.strip().lower()
        return[
            item for item in self.memory
            if query in item["question"].strip().lower() 
            or self.is_similar(query, item["question"])
        ]