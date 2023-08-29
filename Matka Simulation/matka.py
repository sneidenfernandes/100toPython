import random

class matka():


        def __init__(self):
                self.morning_patti = None
                self.evening_patti = None
                self.open = None
                self.close = None
                self.jodi = None

        
        def draw_patti(self, n='morning'):  # Drawing a 'patti.'

                if n == 'morning':
                    morn_p = []
                    for i in range(3):
                        n = random.randint(0,9)
                        morn_p.append(n)
                    self.morning_patti = morn_p
                   
                elif n == 'evening':
                    even_p = []
                    for i in range(3):
                                
                        n = random.randint(0,9)
                        even_p.append(n)
                    self.evening_patti = even_p
                     
        
        def print_patti(self,n='open'):
                if n == 'open':
                        mp = "".join(str(num) for num in self.morning_patti)     
             
                elif n == 'close':
                        ep = "".join(str(num) for num in self.evening_patti) 
                              
                    
        
        def get_jodi(self):   # Computing the Jodi
                no = sum(self.morning_patti)
                no = int(str(no)[-1])
                self.open = no
                
                nc = sum(self.evening_patti)
                nc = int(str(nc)[-1])
                self.close = nc

                self.jodi = int(str(self.open)+str(self.close))


    

                
        
        
        

      




                        



                

        
            

        
                