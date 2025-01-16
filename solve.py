from wordle_words import words
from prosess_result import Game




game=Game(words)


#this wil be the first guess
guess=game.find_best_word(game.count_letters())

you_win=False
for round in range(5):
    print(f'Plis guess "{guess.upper()}"')
    result= input("Write the resulte Green:G Black:B Yellow:Y exp:G,B,B,Y,B: ")
    if result.upper()=="G,G,G,G,G":
        you_win=True
        break
    game.prosess_result(result, guess)
    game.make_new_word_list()
    guess=game.find_best_word(game.count_letters())
else:
    print("____________________________________________________________")
    print("YOU HAVE DONE SOMETHING WRONG NOT ME!!!!!!!!!!!!!!!")


    
    



if you_win:
    print(f"Congratulations the right word was {guess}")






if __name__ == "__main__":
    pass