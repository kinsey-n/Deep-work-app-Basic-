import customtkinter
import tkinter as tk
import time 
from pygame import mixer 





class App(customtkinter.CTk):

    def __init__(self):
        


        super().__init__()

        


        self.title('Deepwork')

        self.button = customtkinter.CTkButton(self, text='Start Timer', command = self.start_clock, height = 50, width = 150, font=('System',25), corner_radius=5,border_width= 10, border_spacing= 20, border_color='black')
        self.button.grid(row=300 , column=400, padx=20, pady=20, sticky="ew", columnspan=2)
        self.button.place(relx = 0.5, rely = 0.5, anchor = 'center')

        self.time_select = customtkinter.CTkOptionMenu(master=self,
                                       values=['Ultra-focus | 60 mins', 'Focused | 40 mins', 'Normal | 25 minutes','Custom'],
                                       command=self.time_selected, dynamic_resizing = True)
        self.time_select.pack(padx=20, pady=10)



        self.seconds, self.minutes, self.hours = 0 , 0 , 0
        self.clock_bool = False


    
    def start_clock(self):
        print(self.clock_bool)
        if self.clock_bool == False: self.clock_bool = True
        else: self.clock_bool = False

        if self.clock_bool == True:
            self.clock()

        


        
        
        

    def clock(self):


        self.timer = customtkinter.CTkLabel(master=self, text=f"{self.minutes:02}:{self.seconds:02}", font=('System',25), height = 50, width = 100)
        self.timer.place(relx=0.5, rely=0.3, anchor = 'center')
        self.button.configure(text= 'Stop Timer')

         
        self.minutes = self.time_selected() if self.time_select != 'Custom' else (self.time_selected())[3:5]

        
        

        while self.minutes > 0 or self.hours > 0 or self.seconds > 0:


            



            self.timer.configure(text = f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}')
            self.update()
            time.sleep(1)
            self.seconds = (self.seconds - 1) if self.seconds != 0 else 59 
            
            
        


    def time_selected(self):
        if self.time_select.get() == 'Ultra-focus | 60 mins': return 60 
        if self.time_select.get() == 'Focused | 40 mins': return 40
        if self.time_select.get() == 'Normal | 25 minutes': return 40

        if self.time_select.get() == 'Custom': 
            self.input = customtkinter.CTkInputDialog(text="Type your time in the form HH:MM:SS:", title="Input Time")
            custom_time = self.input.get_input()
            return custom_time

                


    
                


            
            
        

app = App()



app.mainloop()