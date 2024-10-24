import csv
import datetime
import os

#class expense tracker

class Expensetracker:
    file_to_save = 'expenses.csv'
    
    def __init__(self):
        self.expense = []
        #check the file exists or not
        if not os.path.exists(self.file_to_save):
            with open (self.file_to_save,'w')as file:
                pass     
    # view expenses
    def view_expense(self):
        # if not self.expense:
        #     print ('no items found

        return
    #write to file
    def write_to_file(self,date,amount,item):
        with open(self.file_to_save,'a')as file:
            file.write(f'\n{date}, {amount}, {item}')

    def add_expense(self):
        date = input('enter the date in DDMMYY:')
        amount = input('enter the amount')
        Item = input('enter which category or item:')
        self.write_to_file(date,amount,Item)
        print('added items successfully')


    def main(self):
        #main function 
        while True:
            print("======expense tracker========")
            print('enter your choice:')
            print('1.add expenses')
            print('2. view expense')
            print('3.end choice')
            option = input('select your choice?')

            if option=='1' :
                self.add_expense()
 
            elif option==2:
                self.view_expense()
            elif option==3:
                print('expense tracker is exiting')
                break
            else:
                print('invalid options try again')


if __name__ == "__main__":
    expense = Expensetracker()
    expense.main()


            


        


            

