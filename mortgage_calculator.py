

#### This function will calculate the mortgage####
def calc_monthly_payment(loan_amount,interest_rate,loan_duration_in_months):
    
    #Formula
    M = loan_amount[interest_rate(1+interest_rate)loan_duration_in_months] / [(1+interest_rate)loan_duration_in_months-1]
    print(M)
    #M = L[i(1+i)n] / [(1+i)n-1]
    #   * M = Monthly Payment (what were trying to find out)
    #   * L = Loan Amount (loanAmount)
    #   * I = Interest Rate (for an interest rate of 5%, i = 0.05 (interestCalculation)
    #   * N = Number of Payments (repaymentLength)

if __name__=='__main__':
    
    loan_amount = input("What is the loan amount would you like to borrow?")
    interest_rate=input("What is the interest rate on your loan?")
    loan_duration=input("What is the loan duration in years to repay the loan")

    loan_duration_in_months=float(loan_duration)*12
    print(loan_duration_in_months)
    interest_rate=float(interest_rate)
    loan_amount=float(loan_amount)

    calc_monthly_payment(loan_amount,interest_rate,loan_duration_in_months)

