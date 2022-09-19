

#### This function will calculate the mortgage####
def calc_monthly_payment():
    pass


if __name__=='__main__':
    # calc_monthly_payment()
    loan_amount = input("What is the loan amount would you like to borrow?")
    interest_rate=input("What is the interest rate on your loan?")
    loan_duration=input("What is the loan duration in years to repay the loan")

    loan_duration_in_months=loan_duration*12