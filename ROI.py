class RentalProperty():
    def __init__(self, MonthlyIncome, MonthlyExpenses, MonthlyCashFlow):
        self.Income = MonthlyIncome
        self.Expenses = MonthlyExpenses
        self.CashFlow = MonthlyCashFlow

    def Property(self):
        RentalIncome = input('What is your monthly rental income?')
        print('Monthly Income:', '$', RentalIncome)

        print('For each of the following categories, please list your MONTHLY expense')
        Tax = input('Enter your monthly tax expense')
        print('Tax:', '$',Tax)
        Insurance = input('Enter your monthly insurance cost')
        print('Insurance:', '$', Insurance)
        Utilities = input('Please enter your total utility cost')
        print('Utilities:', '$', Utilities)
        HOA = input('What is the fee of your HOA?')
        print('HOA Fees:', '$', HOA)
        Landscaping = input('What is the monthly cost of your landscaping?')
        print('Landscaping:', '$', Landscaping)
        Vacancy = input('How much do you set aside monthly for vacancy?')
        print('Vacancy:', '$', Vacancy)
        Repairs = input('How much do you set aside monthly for repairs?')
        print('Repairs:', '$', Repairs)
        CapExp = input(
            'How much do you set aside monthly for capital expenses?')
        print('Capital Expenses:', '$', CapExp)
        PropMan = input('What is the monthly cost of your property manager?')
        print('Property Manager:', '$', PropMan)
        Mortgage = input('How much is your monthly mortgage?')
        print('Mortgage:', '$', Mortgage)
        Total_Exp = int(Tax) + int(Insurance) + int(Utilities) + int(HOA) + int(Landscaping) + \
            int(Vacancy) + int(Repairs) + int(CapExp) + \
            int(PropMan) + int(Mortgage)
        print('Total Monthly Expenses:', '$', Total_Exp)
        
        MonthlyCashFlow = int(RentalIncome) - int(Total_Exp)
        print('Total Monthly Cash Flow:', '$', MonthlyCashFlow)

        DownPayment = input('What was your down payment on the property?')
        print('Down Payment:', '$', DownPayment)
        ClosingCosts = input('What is the total of your closing costs?')
        print('Closing Costs:', '$', ClosingCosts)
        RehabBud = input('How much was your rehab budget?')
        print('Rehab Budget:', '$', RehabBud)
        TotalInvestment = int(DownPayment) + int(ClosingCosts) + int(RehabBud)
        print('Total Investment:', '$', TotalInvestment)
        AnnualCashFlow = MonthlyCashFlow*12
        print('Annual Cash Flow:', '$', AnnualCashFlow)
        ROI = int(AnnualCashFlow) / int(TotalInvestment)*100
        print('Your ROI is:', ROI,'%.'' ''Please use this number to make some wise decisions')

    def runner(self):
        while True:
            selection = input(
                'Would you like to use this ROI calculator? Yes or No? ').lower()
            if (selection == 'yes'):
                self.Property()
                break
            elif (selection == 'no'):
                print('Have a great day!')
                break
            elif (selection == 'quit'):
                break
            else:
                print('Invalid input, please try again')


ROI = RentalProperty(MonthlyIncome=(),MonthlyExpenses=(), MonthlyCashFlow=())
ROI.runner()
    


# Write a program that calculates Rental Property ROI
# Using Object Oriented Programming
# four square method:
# INCOME:
    # top left box
    # Rental income
    # laundry machine
    # storage
    # misc
        # xample: DUPLEX $1000/each/month
        # total monthly income = $200
# XPENSES:
    # Bottom Left Box
    #Tax - 150
    #Insurance - 100
    #Utilities - 0
        # electric
        # water
        # sewer
        # garbage
        # gas
    # HOA FEES - 0
    # Lawn/snow care - 0
    # Vacancy  - 5% / (100)
    #repairs - 100
    # CapEx (new roof/heater/etc...) 100
    # Prop MGMT - 10% / 200/month
    #Mortgage: 860
        # TOTAL MONTHLY XPENSES = $1610
# Cash Flow
    # Top Right Box
    #Income - Xpenses
        # 2000-1610
        # MONTHLY CASH FLOW: 390 * 12 = YEARLY CASH FLOW 4680
# Cash On Cash ROI
    # is your money earning a good percent?
    #Downpayment - 40,000
    # closing costs - 3000
    # rehab budget - 7000
    # misc other - 0
        # total investment:  - 50k
        # yearly cashflow = 4680
        # Yearly cashflow divided by total investment:
        # 4690/50000  ROI = 9.36%
