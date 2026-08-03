from datetime import datetime
hour=datetime.now().hour
if hour<12:
    print("Good Morning 🌄")
elif hour<18:
    print("Good Afternoon☀️")  
else:
    print("Good Night sweet dreams 🌙")  
    

