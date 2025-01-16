

class Game():
    def __init__(self, words):
        self.words= words
        self.right_letter=[]
        self.not_possible_letters=[]
        self.letter_right_index_postion={
            
        }
        self.not_letter_index_postion={
            
        }


    def prosess_result(self,result:str, guess:str):

        result= result.split(",")
        for i,letter in enumerate(guess):
            if result[i].upper()=="G":
                self.right_letter.append(letter)
                try:
                    self.letter_right_index_postion[letter].append(i)
                except KeyError:
                    self.letter_right_index_postion[letter]=[i]

            elif result[i].upper()=="B":
                self.not_possible_letters.append(letter)


            elif result[i].upper()=="Y":
                self.right_letter.append(letter)
                try:
                    self.not_letter_index_postion[letter].append(i)
                except KeyError:
                    self.not_letter_index_postion[letter]=[i]

    def prosess_result_from_screen(self,result:list[str], guess:str):

        for i,letter in enumerate(guess):
            if result[i]==" correct":
                self.right_letter.append(letter)
                try:
                    self.letter_right_index_postion[letter].append(i)
                except KeyError:
                    self.letter_right_index_postion[letter]=[i]

            elif result[i]==" absent":
                self.not_possible_letters.append(letter)


            elif result[i]==" present in another position":
                self.right_letter.append(letter)
                try:
                    self.not_letter_index_postion[letter].append(i)
                except KeyError:
                    self.not_letter_index_postion[letter]=[i]

                
            

    def make_new_word_list(self):

        nye_ord=[]
        for word in self.words:
            brukbar_ord=True
            for letter in self.right_letter:
                if letter not in word:
                    brukbar_ord=False
                    break
            
            if brukbar_ord:
                for letter in self.not_possible_letters:
                    if letter in word:
                        brukbar_ord=False
                        break
            
            if brukbar_ord:
                for letter1 in self.letter_right_index_postion:
                    for letter_index in self.letter_right_index_postion[letter1]:
                        if letter1 != word[letter_index]:
                            brukbar_ord=False
                            break
            if brukbar_ord:
                for letter2 in self.not_letter_index_postion:
                    for letter_not_index in self.not_letter_index_postion[letter2]:
                        if letter2 == word[letter_not_index]:
                            brukbar_ord=False
                            break
            

            

            if brukbar_ord:
                nye_ord.append(word)
        self.words=nye_ord



    #this function counts all the letters in the list of words and puts them in dict
    def count_letters(self)->dict[str,int]:
        letter_counter={}

        for word in self.words: 
            for letter in word:
                try: 
                    letter_counter[letter]+=1
                except KeyError:
                    letter_counter[letter]=1
        return letter_counter


    def find_best_word(self,letter_counter:dict)->str:

        beste_ord=""
        beste_sum=0

        #this loop will give all words an value based on how often the letters in the word 
        #comes up in the list of other words 
        for word in self.words: 
            letter_used_sum= 0
            used_letters= []
            for letter in word:
                if letter not in used_letters:
                    letter_used_sum+=letter_counter[letter]
                    used_letters.append(letter)
            if letter_used_sum>beste_sum: 
                beste_sum=letter_used_sum
                beste_ord= word
        
        return beste_ord
            
            
            
        











