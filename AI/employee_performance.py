class EmployeePerformanceEvaluation:
    def __init__(self):
        # A dictionary to store employees data
        self.employees = []
        self.criteria = [
            "Punctuality",
            "Teamwork",
            "Productivity",
            "Quality of Work",
            "Attitude"
        ]
        self.max_score = 5  # Maximum score for each criterion

    def evaluate_employee(self, employee_name, department, role):
        """
        Method to evaluate an employee.
        """
        print(f"\nEvaluating {employee_name} in the {department} Department as {role}")
        
        scores = []
        for criterion in self.criteria:
            while True:
                try:
                    score = int(input(f"Rate {employee_name} for {criterion} (1-5): "))
                    if 1 <= score <= self.max_score:
                        scores.append(score)
                        break
                    else:
                        print("Invalid input. Please enter a score between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer score.")
        
        # Calculate overall score as an average of all criteria scores
        average_score = sum(scores) / len(scores)
        feedback = self.generate_feedback(average_score)
        
        # Store the evaluation in the employee's record
        self.employees.append({
            "name": employee_name,
            "department": department,
            "role": role,
            "scores": dict(zip(self.criteria, scores)),
            "average_score": average_score,
            "feedback": feedback
        })

        print("\nEvaluation complete.")
        print(f"Overall Performance Score for {employee_name}: {average_score:.2f}")
        print(f"Feedback: {feedback}\n")

    def generate_feedback(self, average_score):
        """
        Generate feedback based on the average score.
        """
        if average_score >= 4.5:
            return "Excellent"
        elif average_score >= 3.5:
            return "Good"
        elif average_score >= 2.5:
            return "Average"
        else:
            return "Needs Improvement"

    def view_employee_performance(self, employee_name):
        """
        View the performance of a specific employee.
        """
        for employee in self.employees:
            if employee["name"].lower() == employee_name.lower():
                print(f"\nPerformance Evaluation for {employee_name}:")
                print(f"Department: {employee['department']}")
                print(f"Role: {employee['role']}")
                for criterion, score in employee["scores"].items():
                    print(f"{criterion}: {score}")
                print(f"Average Score: {employee['average_score']:.2f}")
                print(f"Feedback: {employee['feedback']}\n")
                return
        print(f"\nNo records found for {employee_name}.\n")

    def list_all_employees(self):
        """
        List all evaluated employees with their scores and feedback.
        """
        if not self.employees:
            print("No employee evaluations found.")
            return
        
        print("\nList of Evaluated Employees:")
        for employee in self.employees:
            print(f"{employee['name']} - {employee['role']} ({employee['department']})")
            print(f"Average Score: {employee['average_score']:.2f}")
            print(f"Feedback: {employee['feedback']}\n")

    def run(self):
        """
        Main method to interact with the user.
        """
        print("Welcome to the Employee Performance Evaluation System!")
        
        while True:
            print("Options:")
            print("1. Evaluate Employee Performance")
            print("2. View Employee Performance")
            print("3. List All Evaluated Employees")
            print("4. Exit")

            option = input("\nPlease choose an option (1-4): ").strip()

            if option == "1":
                employee_name = input("Enter Employee Name: ").strip()
                department = input("Enter Employee Department: ").strip()
                role = input("Enter Employee Role: ").strip()
                self.evaluate_employee(employee_name, department, role)

            elif option == "2":
                employee_name = input("Enter Employee Name to view performance: ").strip()
                self.view_employee_performance(employee_name)

            elif option == "3":
                self.list_all_employees()

            elif option == "4":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

# Run the Employee Performance Evaluation System
if __name__ == "__main__":
    performance_system = EmployeePerformanceEvaluation()
    performance_system.run()
