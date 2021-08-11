city = input()
sales = float(input())
trade_comission = 0
if sales < 0:
    print("error")
    exit()
if city == 'Sofia':
    if 0 < sales <= 500:
        trade_comission = 0.05 * sales
    elif 500 < sales <= 1000:
        trade_comission = 0.07 * sales
    elif 1000 < sales <= 10000:
        trade_comission = 0.08 * sales
    elif sales > 10000:
        trade_comission = 0.12 * sales
elif city == 'Varna':
    if 0 < sales <= 500:
        trade_comission = 0.045 * sales
    elif 500 < sales <= 1000:
        trade_comission = 0.075 * sales
    elif 1000 < sales <= 10000:
        trade_comission = 0.1 * sales
    elif sales > 10000:
        trade_comission = 0.13 * sales
elif city == 'Plovdiv':
    if 0 < sales <= 500:
        trade_comission = 0.055 * sales
    elif 500 < sales <= 1000:
        trade_comission = 0.08 * sales
    elif 1000 < sales <= 10000:
        trade_comission = 0.12 * sales
    elif sales > 10000:
        trade_comission = 0.145 * sales
else:
    print("error")
    exit()
print(f"{trade_comission:.2f}")
