class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "confidential": [
                "contract", "financial_statement", "research_report"
            ],
            "archive": [
                ("financial_statement", 5),  # Archive after 5 years
                ("research_report", 2)  # Archive after 2 years
            ],
            "department_documents": {
                "HR": ["employee_contract", "salary_report"],
                "Finance": ["financial_statement", "budget_report"],
                "Research": ["research_report", "experiment_notes"]
            }
        }
        self.inference_engine = self.inference

    def inference(self, query):
        """
        Inference engine to process queries based on knowledge base.
        """
        if query.lower() == "which documents are confidential?":
            return self.knowledge_base["confidential"]
        
        elif query.lower() == "which documents should be archived?":
            return [f"{doc[0]} (after {doc[1]} years)" for doc in self.knowledge_base["archive"]]
        
        elif "is confidential" in query.lower():
            doc_type = query.lower().split(" ")[0]
            if doc_type in self.knowledge_base["confidential"]:
                return f"{doc_type} is a confidential document."
            else:
                return f"{doc_type} is not a confidential document."
        
        elif "should be archived" in query.lower():
            doc_type = query.lower().split(" ")[0]
            for doc, years in self.knowledge_base["archive"]:
                if doc_type == doc:
                    return f"{doc_type} should be archived after {years} years."
            return f"No archive rule for {doc_type}."
        
        elif "what documents does" in query.lower():
            department = query.split(" ")[-1]
            if department in self.knowledge_base["department_documents"]:
                return self.knowledge_base["department_documents"][department]
            else:
                return f"Unknown department: {department}"

        else:
            return "I didn't understand your query. Please try again."
    
    def run(self):
        """
        Method to interact with the user and handle queries.
        """
        print("Welcome to the Information Management Expert System!")
        print("You can ask questions such as:")
        print("- Which documents are confidential?")
        print("- Which documents should be archived?")
        print("- Is [document_type] confidential?")
        print("- Should [document_type] be archived?")
        print("- What documents does [department] handle?")
        
        while True:
            query = input("\nPlease enter your query: ").strip()
            if query.lower() == "exit":
                print("Exiting the system. Goodbye!")
                break
            response = self.inference_engine(query)
            print("Expert System:", response)

# Run the Expert System
if __name__ == "__main__":
    expert_system = ExpertSystem()
    expert_system.run()
