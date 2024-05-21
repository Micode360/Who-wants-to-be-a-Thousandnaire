from music import Intro
from musicPath import introMusic
from utils import currentQuestion
from textpath import colored_text
from Remarkspath import remarks
questions = [
    {
        "question": "Which of these is not a country?",
        "options": ["Venezuela", "Canada", "Qatar", "Toronto"],
        "answer": "d"
    },
    {
        "question": "What is the capital of Nigeria?",
        "options": ["Lagos", "Abuja", "Kano", "Port Harcourt"],
        "answer": "b"
    },
    {
        "question": "Which Nigerian musician is known as the 'African Giant'?",
        "options": ["Wizkid", "Davido", "Burna Boy", "Tiwa Savage"],
        "answer": "c"
    },
    {
        "question": "What is the currency of Nigeria?",
        "options": ["Dollar", "Cedi", "Naira", "Pound"],
        "answer": "c"
    },
    {
        "question": "Who is the current President of Nigeria as of 2024?",
        "options": ["Goodluck Jonathan", "Muhammadu Buhari", "Yemi Osinbajo", "Bola Tinubu"],
        "answer": "d"
    },
    {
        "question": "Which Nigerian city is known as the 'Centre of Excellence'?",
        "options": ["Lagos", "Abuja", "Ibadan", "Enugu"],
        "answer": "a"
    },
    {
        "question": "What is the main staple food in Nigeria?",
        "options": ["Rice", "Potatoes", "Pasta", "Bread"],
        "answer": "a"
    },
    {
        "question": "Which Nigerian state is famous for its oil production?",
        "options": ["Lagos", "Kano", "Rivers", "Oyo"],
        "answer": "c"
    },
    {
        "question": "What is the official language of Nigeria?",
        "options": ["Hausa", "Yoruba", "Igbo", "English"],
        "answer": "d"
    },
    {
        "question": "Which Nigerian author wrote 'Things Fall Apart'?",
        "options": ["Chinua Achebe", "Wole Soyinka", "Chimamanda Ngozi Adichie", "Ben Okri"],
        "answer": "a"
    }
]

prize_unicode = [
    "\u20A6" + "100",
    "\u20A6" + "200",
    "\u20A6" + "300",
    "\u20A6" + "400",
    "\u20A6" + "500",
    "\u20A6" + "600",
    "\u20A6" + "700",
    "\u20A6" + "800",
    "\u20A6" + "900",
    "\u20A6" + "1000",
]

print(colored_text("WELCOME TO WHO WANTS TO BE A THOUSANDNAIRE!!!", "30;44"))

def Main():
    score = 0
    for item in questions:
        currentQuestion(item)
        choice = input("Choose a/b/c/d: ")
        if choice != item["answer"]:
            print("Nice try but you failed")
            print(f"You just won {prize_unicode[score] if score != 0 else '₦0'}")
            break
        else:
            score += 1
            if score == len(questions):
                print("=====================================================")        
                print(f"YES!!! You did it. You are a thousandnaire.")
                print(f"You just won {prize_unicode[score - 1]}")
                print(f"Thank you for playing :)")
                print("=====================================================")
                break
            else:
                print("=====================================================")        
                remarks()
                print(f"You now have {prize_unicode[score - 1]}")
                print("=====================================================")
                option = input("Do you want to continue(yes) or walk away(no)? choose(yes/no): ")
                if option == "yes":
                    continue
                elif option == "no":
                    print("=====================================================")
                    print(f"A fair decision {prize_unicode[score - 1]}")
                    print(f"Thanks for playing")
                    print("=====================================================")
                    break
                else:
                    print("Invalid option. Continuing by default.")
                    continue

Intro(introMusic)

# Running program
Main()
