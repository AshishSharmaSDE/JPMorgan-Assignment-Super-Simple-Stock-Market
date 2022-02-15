from services.stock_services import Stock


def user_stock_symbol():
    stock_symbol = input("\nChoose a stock symbol:" +
                         "\n1. TEA " +
                         "\n2. POP " +
                         "\n3. ALE " +
                         "\n4. GIN " +
                         "\n5. JOE" +
                         "\n>")
    return stock_symbol


def user_price_input():
    stock_price = input("\nEnter price \n>")
    return stock_price


def calculate_divident():
    stock_symbol = user_stock_symbol()
    stock_price = user_price_input()

    status, result = Stock().calc_divident(stock_symbol, stock_price)

    if status:
        print("Dividend Yield :", result)
    else:
        print(result)


def calculate_pe_ratio():
    stock_symbol = user_stock_symbol()
    stock_price = user_price_input()
    
    status_code, result = Stock().calc_pe_ratio(stock_symbol, stock_price)
    
    if status:
            print("P/E Ratio :", result)
    else:
        print(result)
        

def record_trade():
    stock_symbol = user_stock_symbol()
    share_quantity = input("Quantity of shares \n")
    indicator = raw_input("Choose a indicator :" +
                    "\n1. BUY " +
                    "\n2. SELL" +
                    "\n>")
    trade_price = user_price_input()
    
    Stock().record_trade(stock_symbol, share_quantity, indicator, trade_price)