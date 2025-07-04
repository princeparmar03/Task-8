print("💪 Hello! I'm MotivationBot. Let me inspire you. Type 'exit' to end.")

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("MotivationBot: Remember, you're stronger than you think. Goodbye!")
        break
    elif "sad" in msg or "depressed" in msg:
        print("MotivationBot: It's okay to feel that way. You're not alone. Keep going!")
    elif "motivate me" in msg or "inspire" in msg:
        print("MotivationBot: Push yourself, because no one else is going to do it for you. ")
    elif "tired" in msg:
        print("MotivationBot: Rest if you must, but don’t you quit!")
    else:
        print("MotivationBot: Every day is a new chance to grow.")
