class HospitalExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "symptoms_diseases": {
                "fever": ["flu", "malaria", "dengue"],
                "cough": ["flu", "tuberculosis"],
                "headache": ["migraine", "flu", "tension_headache"],
                "shortness of breath": ["pneumonia", "asthma", "COPD"],
                "fatigue": ["anemia", "depression", "hypothyroidism"],
            },
            "disease_treatment": {
                "flu": "Rest, plenty of fluids, over-the-counter medications like ibuprofen.",
                "malaria": "Anti-malarial drugs, rest, fluid intake.",
                "dengue": "Rest, pain relievers, and fluids. In severe cases, hospitalization.",
                "migraine": "Pain relievers, anti-nausea medications, rest in a quiet room.",
                "tuberculosis": "Antibiotics for 6-9 months.",
                "pneumonia": "Antibiotics and rest.",
                "asthma": "Inhalers and bronchodilators.",
                "COPD": "Inhalers, oxygen therapy, and pulmonary rehabilitation.",
                "anemia": "Iron supplements and dietary changes.",
                "depression": "Therapy, antidepressants, and lifestyle changes.",
                "hypothyroidism": "Thyroid hormone replacement therapy.",
            },
            "department_guidelines": {
                "fever": "General Medicine or Infectious Disease Department.",
                "cough": "General Medicine, Pulmonology.",
                "headache": "Neurology, General Medicine.",
                "shortness of breath": "Pulmonology, Cardiology.",
                "fatigue": "Endocrinology, Psychiatry.",
            }
        }
        self.inference_engine = self.inference

    def inference(self, query):
        """
        Inference engine to process queries based on knowledge base.
        """
        query = query.lower()

        # Query for disease based on symptoms
        if "what disease" in query or "possible diseases" in query:
            symptom = query.split("for")[1].strip()
            if symptom in self.knowledge_base["symptoms_diseases"]:
                diseases = self.knowledge_base["symptoms_diseases"][symptom]
                return f"Possible diseases for {symptom} are: {', '.join(diseases)}."
            else:
                return "Sorry, I don't have information for that symptom."

        # Query for treatment based on disease
        elif "treatment for" in query:
            disease = query.split("for")[1].strip()
            if disease in self.knowledge_base["disease_treatment"]:
                treatment = self.knowledge_base["disease_treatment"][disease]
                return f"Treatment for {disease}: {treatment}"
            else:
                return f"Sorry, I don't have treatment information for {disease}."

        # Query for the right department based on symptoms
        elif "which department" in query:
            symptom = query.split("for")[1].strip()
            if symptom in self.knowledge_base["department_guidelines"]:
                department = self.knowledge_base["department_guidelines"][symptom]
                return f"Patients with {symptom} should be referred to the {department}."
            else:
                return "Sorry, I don't have department information for that symptom."

        # General information
        elif "hospital" in query or "facility" in query:
            return "We provide comprehensive healthcare services, including diagnostics, treatments, and specialized departments."
        
        elif "exit" in query:
            return "Thank you for using the Hospital Expert System. Goodbye!"

        else:
            return "I didn't understand your query. Please try again."

    def run(self):
        """
        Method to interact with the user and handle queries.
        """
        print("Welcome to the Hospital and Medical Facility Expert System!")
        print("You can ask questions such as:")
        print("- What disease could cause [symptom]?")
        print("- What is the treatment for [disease]?")
        print("- Which department handles [symptom]?")
        print("- General hospital information.")
        print("- Type 'exit' to quit the system.")

        while True:
            query = input("\nPlease enter your query: ").strip()
            if "exit" in query.lower():
                print(self.inference_engine(query))
                break
            else:
                response = self.inference_engine(query)
                print("Expert System:", response)

# Run the Expert System
if __name__ == "__main__":
    expert_system = HospitalExpertSystem()
    expert_system.run()
