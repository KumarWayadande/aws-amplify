import time

class SimpleChatbot:
    def __init__(self):
        self.name = "CustomerBot"
    
    def greet(self):
        print("Hello! Welcome to our Customer Support.")
        time.sleep(1)
        print("I'm", self.name, "and I'll be assisting you today.")
    
    def answer_questions(self, user_input):
        user_input = user_input.lower()
        
        if "hello" in user_input or "hi" in user_input:
            return "Hi! How can I assist you today?"
        
        elif "what is your business" in user_input:
            return "We are a customer service company that provides 24/7 support for various industries."
        
        elif "what services do you offer" in user_input:
            return "We offer live chat support, phone support, email support, and helpdesk services."
        
        elif "contact support" in user_input:
            return "You can reach our support team via email at support@company.com or call us at 123-456-7890."
        
        elif "hours of operation" in user_input:
            return "We are available 24/7, every day of the year!"
        
        elif "thank you" in user_input or "thanks" in user_input:
            return "You're welcome! Let me know if you need further assistance."
        
        elif "bye" in user_input or "goodbye" in user_input:
            return "Goodbye! Have a great day! :)"
        
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def run(self):
        self.greet()
        
        while True:
            user_input = input("\nYou: ")
            if "bye" in user_input.lower() or "goodbye" in user_input.lower():
                print("CustomerBot: " + self.answer_questions(user_input))
                break
            else:
                print("CustomerBot: " + self.answer_questions(user_input))


# Example usage of the chatbot
if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.run()
