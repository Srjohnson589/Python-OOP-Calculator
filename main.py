# This is a OOP program that calculates the Return on Investment of a rental property
# based on input from the user

#it has capabilities to add income, expenses, and finally investment amount
#it will either print out the ROI at the end, or store it for you and you can add another property
#when you are finished you will get a print out of all the ROIs on your properties

class Rental_Calc:

    def __init__(self):
        self.all_props = {}
        self.prop_income = 0
        self.prop_expenses = 0
        self.prop_cashflow = 0
        self.prop_invest = 0
        self.prop_roi = 0

    def validate(self, question):
        try:
            result = input(question).strip()
            return int(result)
        except:
            if result == 'quit':
                return 'quit'
            print("Please enter positive digits. Or type 'quit'.")

    def income(self):
        print("Let's look at all the types of income you could receive from this property. If the answer is none, please enter 0.")
        # list of questions
        questions = ["How much would you charge in rent per month (total if split property)? ",
                    "How much would you charge for laundry per month (total if split property)? ",
                    "How much would you charge for storage per month (total)? ",
                    "How much in other misc income might you receive from this property per month? "
                    ]
        current = 0
        while current < len(questions):
            ans = self.validate(questions[current])
            if ans >= 0 and ans != 'quit':
                self.prop_income += ans
                current += 1
            elif ans == 'quit':
                return 'quit'

    def expenses(self):
        print("Now let's look at all the types of expenses you could pay on this property. If the answer for a category is none, please enter 0.")
        # list of questions
        questions = ["How much would you pay in taxes on the property per month? ",
                    "How much would you pay for insurance per month? ",
                    "How much would you pay for utilities (electric, water, sewer, garbage, gas) per month? \n(If the tenant will pay, enter 0) ",
                    "How much would you pay in HOA fees per month? ",
                    "How much would you pay for lawncare/snow removal per month? ",
                    "How much would you put aside for vacancy per month? (recommended 5% of total rent) ",
                    "How much would you pay or set aside for repairs per month? ",
                    "How much would you pay or set aside for CapEx per month? (long term maintenance) ",
                    "How much would you pay for property manangement per month? ",
                    "How much would you pay on the mortgage per month? "
                    ]
        current = 0
        while current < len(questions):
            ans = self.validate(questions[current])
            if ans >= 0 and ans != 'quit':
                self.prop_expenses += ans
                current += 1
            elif ans == 'quit':
                return 'quit'

    def invest(self):
        print("We're almost there! After these final questions about your initial investment, we will have your ROI %.")
        # list of questions
        questions = ["What would be your initial down payment on the property? ",
                    "How much would closing costs be? ",
                    "How much would you spend on rehabilitation cost (painting, remodeling)? ",
                    "How much would you spend in other miscellaneous initial costs? "
                    ]
        current = 0
        while current < len(questions):
            ans = self.validate(questions[current])
            if ans >= 0 and ans != 'quit':
                self.prop_invest += ans
                current += 1
            elif ans == 'quit':
                return 'quit'
            
    def roi(self):
        self.prop_cashflow = (self.prop_income - self.prop_expenses)*12
        try:
            self.prop_roi = self.prop_cashflow / self.prop_invest
        except:
            self.prop_roi = self.prop_cashflow
        print(f"Total income : ${self.prop_income}")
        print(f"Total expenses : ${self.prop_expenses}")
        print(f"Calculated annual cashflow: ${self.prop_cashflow}")
        print(f"Total investment: ${self.prop_invest}")
        print("-------------------------")
        print(f"ROI = {self.prop_roi:.2f}%")


    def print_out(self):
        print("Here are the investment properties we looked at today:")
        print("--------------------------")
        for key, value in self.all_props.items():
            if type(value) == str:
                print(f"{key} : {value}")
            else:
                print(f"{key} : {value:.2f}%")

    def runner(self):
        print('Welcome to your Rental Property ROI Calculator!')
        while True:
            self.prop_income = self.prop_expenses = self.prop_cashflow = self.prop_invest = self.prop_roi = 0
            while True:
                name = input('What would you like to call this property? ').strip()
                if name.lower() == 'quit':
                    return self.end()
                if name in self.all_props:
                    print("Please choose a unique name for this calculation. ")
                else:
                    self.all_props[name] = 'Unfinished'
                    break
            if self.income() == 'quit':
                break
            if self.expenses() == 'quit':
                break
            if self.invest() == 'quit':
                break
            print(f"You did it! Given the following for {name}:")
            self.roi()
            self.all_props[name] = str(self.prop_roi)
            restart = input("Would you like to look at another property, or try this property with different numbers? ").strip()
            if restart.lower() in ['no', 'quit']:
                break
        self.end()

    def end(self):
        self.print_out()
        print("--------------------------")
        print("Goodbye!")


myproperty = Rental_Calc()

myproperty.runner()





