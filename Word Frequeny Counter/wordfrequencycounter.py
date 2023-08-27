import string # to strip the punction from the text inorder to make it efficient for analysis.

class word_frequency_counter():

    def __init__(self):
        self.text = None
        self.frequency = {}



    def read(self,filename):  # Reads the text file.
        try:
            with open(filename, 'r') as file:
                self.text = file.read()

        except FileNotFoundError:
            print('File not found! Please Enter a valid filename!')


    def display(self):  # Prints the content of the text file.
        print(self.text)


            

    def analyse_frequency(self):   # Prints the frequency of each word in the text file.
        words = self.text.lower().split()
        
        for word in words:
            word = word.strip(string.punctuation)

            if word in self.frequency:
                self.frequency[word] += 1
            else:
                self.frequency[word] = 1

        for word,freq in self.frequency.items():
            print(f"{word}:{freq}")


    def analyse_word(self,text):  #Prints the frequency of a specefic word in the text file. 
        print(self.frequency[str(text)])

    



if __name__ == '__main__':
    
    cream = word_frequency_counter()      
    cream.read('cream.txt')              
    cream.analyse_frequency()
    cream.analyse_word("cream")
  