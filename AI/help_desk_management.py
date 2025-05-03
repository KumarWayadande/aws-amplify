class HelpDeskManagementSystem:
    def __init__(self):
        self.knowledge_base = {
            "account_issues": [
                "Forgot password", "Account locked", "Unable to login"
            ],
            "technical_issues": [
                "System crash", "Software not working", "Network issues"
            ],
            "billing_issues": [
                "Incorrect billing", "Refund request", "Overcharged"
            ],
            "solutions": {
                "Forgot password": "Please use the 'Forgot Password' feature on the login page.",
                "Account locked": "Please try resetting your password. If issue persists, contact support.",
                "Unable to login": "Please check if your credentials are correct or reset your password.",
                "System crash": "Try restarting your system. If issue continues, reinstall the application.",
                "Software not working": "Ensure your software is updated to the latest version.",
                "Network issues": "Check your network connection and try again. If problem persists, contact IT support.",
                "Incorrect billing": "Please contact our billing department with your account details for assistance.",
                "Refund request": "Please contact our support team with your order number to process a refund.",
                "Overcharged": "Contact billing support for clarification or refund."
            },
            "ticket_status": ["Open", "In Progress", "Resolved"]
        }
        self.tickets = []
        self.inference_engine = self.inference
    
    def inference(self, ticket_description):
        """
        Inference engine to process the ticket based on the description.
        """
        ticket_description = ticket_description.lower()

        # Categorizing the ticket based on keywords
        if any(issue.lower() in ticket_description for issue in self.knowledge_base["account_issues"]):
            category = "Account Issues"
        elif any(issue.lower() in ticket_description for issue in self.knowledge_base["technical_issues"]):
            category = "Technical Issues"
        elif any(issue.lower() in ticket_description for issue in self.knowledge_base["billing_issues"]):
            category = "Billing Issues"
        else:
            category = "General Query"
        
        # Assigning priority based on issue description
        if "critical" in ticket_description or "urgent" in ticket_description:
            priority = "High"
        elif "minor" in ticket_description or "slow" in ticket_description:
            priority = "Low"
        else:
            priority = "Medium"

        return category, priority

    def create_ticket(self, description):
        """
        Method to create a ticket based on user description.
        """
        category, priority = self.inference(description)
        ticket = {
            "id": len(self.tickets) + 1,
            "description": description,
            "category": category,
            "priority": priority,
            "status": "Open",
            "solution": self.knowledge_base["solutions"].get(description.lower(), "Solution not available.")
        }
        self.tickets.append(ticket)
        return ticket

    def resolve_ticket(self, ticket_id):
        """
        Mark the ticket as resolved.
        """
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                ticket["status"] = "Resolved"
                return ticket
        return "Ticket ID not found."

    def view_ticket(self, ticket_id):
        """
        View a specific ticket's details.
        """
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                return ticket
        return "Ticket ID not found."
    
    def list_tickets(self):
        """
        List all tickets.
        """
        return self.tickets

    def run(self):
        """
        Method to interact with the user and handle ticket-related tasks.
        """
        print("Welcome to the Help Desk Management System!")
        print("You can create a ticket, view tickets, or resolve issues.")
        
        while True:
            print("\nOptions:")
            print("1. Create a new ticket")
            print("2. View a ticket")
            print("3. Resolve a ticket")
            print("4. List all tickets")
            print("5. Exit")
            
            option = input("\nPlease choose an option (1-5): ").strip()

            if option == "1":
                description = input("Describe the issue you are facing: ").strip()
                ticket = self.create_ticket(description)
                print(f"\nTicket created successfully. Ticket ID: {ticket['id']}")
                print(f"Category: {ticket['category']}")
                print(f"Priority: {ticket['priority']}")
                print(f"Solution: {ticket['solution']}")

            elif option == "2":
                ticket_id = int(input("Enter Ticket ID to view: ").strip())
                ticket = self.view_ticket(ticket_id)
                print(ticket)

            elif option == "3":
                ticket_id = int(input("Enter Ticket ID to resolve: ").strip())
                ticket = self.resolve_ticket(ticket_id)
                print(ticket)

            elif option == "4":
                tickets = self.list_tickets()
                for ticket in tickets:
                    print(f"\nTicket ID: {ticket['id']}, Status: {ticket['status']}, Priority: {ticket['priority']}")
                    print(f"Description: {ticket['description']}")
                    print(f"Category: {ticket['category']}")
                    print(f"Solution: {ticket['solution']}")

            elif option == "5":
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

# Run the Help Desk Management System
if __name__ == "__main__":
    help_desk_system = HelpDeskManagementSystem()
    help_desk_system.run()
