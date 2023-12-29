def optimal_reinvestment_time(fees, liquidity, gas, days=365):
    return_percent = fees / liquidity

    max_return = 0
    optimal_day = 0

    for day in range(1, days+1):
        total_return = 0
        money_in_pool = liquidity
        returns = 0
        for dayReturns in range(1, days+1):
            daily_return = (return_percent * money_in_pool)
            total_return += daily_return
            returns += daily_return
            if dayReturns % day == 0:  # reinvest returns every 'day' days
                money_in_pool += returns - (2*gas)
                returns = 0

        # print(f"Day: {day} Return: {total_return}")
        if total_return > max_return:
            max_return = total_return
            optimal_day = day

    return optimal_day, max_return

fees = 1.88
liquidity = 483.87
gas = 0.08

optimal_day, max_return = optimal_reinvestment_time(fees, liquidity, gas)
print(f"The optimal day to reinvest is: {optimal_day} with a return of: {max_return}")
