
import json
import pygame
import functions
pygame.mixer.init()
with open(r"C:\Users\HP\Desktop\week2\Who-wants-to-be-a-Thousandnaire\question.json", "r") as f:
    questions = json.load(f)

prize_unicode = []
for prize in range(10):
    prize_unicode.append( f"\u20A6{(prize+1)*100}")  



print(functions.colored_text("WELCOME TO WHO WANTS TO BE A THOUSANDNAIRE!!!", "30;44"))


soundwronganswer = pygame.mixer.Sound(r"C:\Users\HP\Desktop\week2\Who-wants-to-be-a-Thousandnaire\media\wrong_answer.mp3")
Introsound = pygame.mixer.Sound(r"C:\Users\HP\Desktop\week2\Who-wants-to-be-a-Thousandnaire\media\Who_Wants_To_Be_A_Millionaire Full_Theme.mp3")

def Main():
    Introsound.play()
    score = 0
    for item in questions:
        functions.currentQuestion(item)
        choice = input("Choose a/b/c/d: ")
        if choice != item["answer"]:
            Introsound.stop()
            soundwronganswer.play()
            print("Nice try but you failed")
            print(f"You just won  {prize_unicode[score] if score != 0 else '₦0'}")
               
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
                functions.remarks()
                print(f"You now have {prize_unicode[score - 1]}")
                print("=====================================================")
                option = input("Do you want to continue(c) or walk away(w)? choose(c/w): ")
                if option == "c":
                    continue
                elif option == "w":
                    print("=====================================================")
                    print(f"A fair decision {prize_unicode[score - 1]}")
                    print(f"Thanks for playing")
                    print("=====================================================")
                    break
                else:
                    print("Invalid option. Continuing by default.")
                    continue
# Running program
Main()
