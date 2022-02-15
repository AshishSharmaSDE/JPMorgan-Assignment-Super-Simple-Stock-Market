from utilities import utilities as util


def get_user_input():
    user_input = str(input("\nEnter the number of the Option you want:" +
                           "\n1. Calculate dividend yield" +
                           "\n2. Calculate the P/E Ratio"
                           "\n3. Record Trade" +
                           "\n4. Calculate Volume Weighted Stock Price "
                           "\n5. Calculate the GBCE All Share Index"
                           "\n>"))
    return user_input


def redirect_per_option():
    user_input = get_user_input()
    if user_input == "1":
        util.calculate_divident()
    elif user_input == "2":
        util.calculate_pe_ratio()
    elif user_input == "3":
        util.record_trade()
    elif user_input == "4":
        util.stock_price()
    elif user_input == "5":
        util.calculate_share_index()
    else:
        print("Wrong input. Try Again")
    
    retry = input("\nWould you like to try again.(Y/N)\n>")
    if retry == "Y":
        redirect_per_option()
    elif retry == "N":
        pass
    else:
        print("Wrong Input. Please type Y/N.")


def main():
    redirect_per_option()


if __name__ == '__main__':
    main()
    
