from services.stock_services import Stock
from .validater import validate_inputs as vi

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
    validater = vi.validate(int(stock_symbol), "stock_symbol")

    if validater:
        stock_price = user_price_input()
        status, result = Stock().calc_divident(stock_symbol, stock_price)
        if status:
            print("Dividend Yield :", result)
        else:
            print(result)
    else:
        print("Wrong Input. Try Again!!")


def calculate_pe_ratio():
    stock_symbol = user_stock_symbol()
    validater = vi.validate(int(stock_symbol), "stock_symbol")
    
    if validater:
        stock_price = user_price_input()
        status, result = Stock().calc_pe_ratio(stock_symbol, stock_price)
        
        if status:
                print("P/E Ratio :", result)
        else:
            print(result)
    else:
        print("Wrong Input. Try Again!!")

def record_trade():
    stock_symbol = user_stock_symbol()
    symbol_validater = vi.validate(int(stock_symbol), "stock_symbol")
    

    indicator = input("Choose a indicator :" +
                    "\n1. BUY " +
                    "\n2. SELL" +
                    "\n>")
    indicator_validater = vi.validate(int(indicator), "indicator")
    
    if symbol_validater and indicator_validater:
        share_quantity = input("Quantity of shares \n")
        trade_price = user_price_input()
        
        status, result = Stock().record_trade(stock_symbol, share_quantity, indicator, trade_price)
        if status:
                print("Trade_record  :", result)
        else:
            print(result)
    else:
        print("Wrong Input. Try Again!!")
    

def stock_price():
    stock_symbol = user_stock_symbol()
    symbol_validater = vi.validate(int(stock_symbol), "stock_symbol")
    if symbol_validater:
        Stock().stock_price(stock_symbol)
    

def calculate_share_index():
    Stock().share_index()