import emoji
from music import Intro
from musicPath import introMusic
from utils import currentQuestion
from textpath import colored_text
from Remarkspath import remarks
from questions import questions
from price import prize_unicode


print(colored_text("WELCOME TO WHO WANTS TO BE A THOUSANDNAIRE!!!", "30;44"))

def Main():
    score = 0
    for item in questions:
        currentQuestion(item)
        choice = input("Choose a/b/c/d: ").lower()
        if choice != item["answer"]:
            print("Nice try but you failed")
            print(f"You just won 👏 {prize_unicode[score] if score != 0 else '₦0'}")
            break
        else:
            score += 1
            if score == len(questions):
                print("=====================================================")        
                #print(f"You just won {prize_unicode[score - 1]}")
                print(f"Congratulations! You did it!  👏🎉🎉You just won {prize_unicode[score - 1]}")
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

# # Running program
Main()

