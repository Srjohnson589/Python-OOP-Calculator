# This is a OOP program that calculates the Return on Investment of a rental property
# based on input from the user

#it has capabilities to add income, expenses, and finally investment amount
#it will either print out the ROI at the end, or store it for you and you can add another property
#when you are finished you will get a print out of all the ROIs on your properties

class Rental_Calc:

    def __init__(self):
        self.props = {}

    def income(self):
        print("Let's look at all the types of income you could receive from this property. If the answer is none, please enter 0.")
        inc_1 = input("How much would you charge in rent per month (total if split property)?").strip()
        try:
            inc_1 = int(inc_1)
            print("finished the try block")
        except:
            if inc_1 == 'quit':
                print("You typed quit")
                return 'quit'
            print("Please enter positive digits for the income. Or type 'quit'")
            # self.income()
        # inc_2 = input("How much would you charge for laundry per month (total if split property)?").strip()
        # inc_3 = input("How much would you charge for storage per month (total)?")
        # inc_4 = input("How much in other misc income might you receive from this property per month?")
        # self.total_inc = inc_1 + inc_2 + inc_3 + inc_4
        # return 'quit'

    def expenses(self):
        print("Now let's look at all the types of expenses you could pay on this property. If the answer for a category is none, please enter 0.")
        while True:
            exp_1 = input("How much would you pay in taxes on the property per month?")
            self.check_valid(exp_1, self.expenses())
            exp_2 = input("How much would you pay for insurance per month?")
            self.check_valid(exp_2, self.expenses())
            exp_3 = input("How much would you pay for utilities (electric, water, sewer, garbage, gas) per month? \n(If the tenant will pay, enter 0)")
            self.check_valid(exp_3, self.expenses())
            exp_4 = input("How much would you pay in HOA fees per month?")
            self.check_valid(exp_4, self.expenses())
            exp_5 = input("How much would you pay for lawncare/snow removal per month?")
            self.check_valid(exp_5, self.expenses())
            exp_6 = input("How much would you put aside for vacancy per month? (recommended 5% of total rent)")
            self.check_valid(exp_6, self.expenses())
            exp_7 = input("How much would you pay or set aside for repairs per month?")
            self.check_valid(exp_7, self.expenses())
            exp_8 = input("How much would you pay or set aside for CapEx per month? (long term maintence)")
            self.check_valid(exp_8, self.expenses())
            exp_9 = input("How much would you pay for property manangement per month?")
            self.check_valid(exp_9, self.expenses())
            exp_10 = input("How much would you pay for the mortgage per month?")
            self.check_valid(exp_10, self.expenses())
            self.total_exp = sum(exp_1, exp_2, exp_3, exp_4, exp_5, exp_6, exp_7, exp_8, exp_9, exp_10)
            break

    def cashflow(self):
        pass

    def roi(self):
        pass

    def print_out(self):
        print("Here are the investment properties we looked at today:")
        print("--------------------------")
        for key, value in self.props.items():
            if type(value) == str:
                print(f"{key} : {value}")
            else:
                print(f"{key} : {value:.2f / 100}%")

    def runner(self):
        print('Welcome to your Rental Property ROI Calculator!')
        while True:
            name = input('What would you like to call this property?').strip()
            if name.lower() == 'quit':
                break
            # reinitializing in case there was a prior property
            self.props[name] = 'Unfinished'
            self.total_inc = self.total_exp = 0
            self.income()
            if self.income() == 'quit':
                break
            self.expenses()
            if self.expenses() == False:
                break
            self.cashflow()
            self.roi()
            if self.roi() == False:
                break
            break
        self.end()

    def end(self):
        self.print_out()
        print("--------------------------")
        print("Goodbye!")


myproperty = Rental_Calc()

myproperty.runner()





