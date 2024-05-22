import random

def currentQuestion(item):
    print(f"{item['question']}")
    print(f"a. {item['options'][0]}")
    print(f"b. {item['options'][1]}")
    print(f"c. {item['options'][2]}")
    print(f"d. {item['options'][3]}")
    return True

def remarks():
    opt = ["Outstanding", "Good job", "Right on."]
    print(random.choice(opt))
    return True

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"