def reply(text: str) -> str:
    if "exam" in text:
        return "You should complete your syllabus first"
    elif "rain" in text:
        return "Carry an umbrella"
    elif "late" in text:
        return "You should start early"
    
text = input("Matching Keyword: ").lower()
print(reply(text))
