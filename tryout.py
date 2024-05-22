import store
import time
import random
import functions
from music import Intro, StopMusic, Lose, Winner,Final
from musicPath import introMusic



def Main():
    Intro(introMusic)
    
    score = 0
    questions = store.questions.copy()  # Make a copy of the questions list to avoid modifying the original
    random.shuffle(questions)
    total_questions = len(store.questions)

    

    for item in questions:
        
        functions.currentQuestion(item)

        while True : 
            choice = input("Choose a/b/c/d: ").lower()
            
            StopMusic()
            Final()

            sure = input("Is that your final anwer yes(y) or no(n)? choose(y/n): ").lower()
            
            
            if sure == "y":
                        time.sleep(3)
            else:
                 continue
                 

            if choice not in ['a', 'b', 'c', 'd']:
                print("Invalid choice. Please choose a/b/c/d.")

                continue
            else :
                break

            
                
            
                        
                

        

        if choice != item["answer"]:
            StopMusic()
            Lose()
            print("Nice try but you failed")
            print(f"You just won {store.prize_unicode[score] if score != 0 else '₦0'}")
            time.sleep(7)
            break
                

        else:
            score += 1
            if score == total_questions:
                StopMusic()
                Winner()
                print("=====================================================")        
                print(f"YES!!! You did it. You are a thousandnaire.")
                print(f"You just won {store.prize_unicode[score - 1]}")
                print(f"Thank you for playing :)")
                print("=====================================================")
                time.sleep(7)
                break
            else:
                StopMusic()
                Winner()
                print("=====================================================")        
                functions.remarks()
                print(f"You now have {store.prize_unicode[score - 1]}")
                print("=====================================================")
                option = input("Do you want to continue(c) or walk away(w)? choose(c/w): ").lower()
                
                if option == "c":
                    Intro(introMusic)

                    continue
                elif option == "w":
                    Lose()
                    print("=====================================================")
                    print(f"A fair decision {store.prize_unicode[score - 1]}")
                    print(f"Thanks for playing")
                    print("=====================================================")
                    time.sleep(7)
                    break
                else:
                    print("Invalid option. Continuing by default.")
                    continue



# Running program
Main()
