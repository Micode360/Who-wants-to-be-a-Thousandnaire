import random

def currentQuestion(item):
    print(f"{item['question']}")
    print(f"{item['selector'][0]} {item['options'][0]}")
    print(f"{item['selector'][1]} {item['options'][1]}")
    print(f"{item['selector'][2]} {item['options'][2]}")
    print(f"{item['selector'][3]} {item['options'][3]}")
    return True

def remarks():
    opt = ["Outstanding", "Good job", "Right on."]
    print(random.choice(opt))
    return True

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

print(colored_text("WELCOME TO WHO WANTS TO BE A THOUSANDNAIRE!!!", "30;44"))
