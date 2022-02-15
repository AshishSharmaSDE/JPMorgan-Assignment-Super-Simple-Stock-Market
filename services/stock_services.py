import csv

gbce_csv_reader = list(csv.DictReader(open('./data/gbce.csv')))

stock_symbol_mapping = {
    1: "TEA",
    2: "POP",
    3: "ALE",
    4: "GIN",
    5: "JOE"
}


class Stock():
    def calc_divident(self, symbol, price):
        stock_symbol = stock_symbol_mapping.get(int(symbol), None)
        if stock_symbol is None:
            return False, "Enter Valid Stock Symbol"

        try:
            if float(price) == 0.0:
                return False, "Enter valid price"
        except:
            return False, "Enter valid price"

        for gbce_stock in gbce_csv_reader:
            if gbce_stock['stock_symbol'] == str(stock_symbol):
                if gbce_stock['stock_type'] == "Common":
                    try:
                        divident = float(gbce_stock.get(
                            'last_divident', 0)) / float(price)
                    except ZeroDivisionError:
                        divident = 0
                else:
                    try:
                        divident = (float(gbce_stock.get('fixed_divident', 0))/100) * \
                            float(gbce_stock.get('par_value', 0)) / \
                            float(price)
                    except ZeroDivisionError:
                        divident = 0

                return True, divident

    def calculate_pe_ratio(self, symbol, price):
        status, result = self.calc_divident(symbol, price)

        if not status:
            return status, result
        else:
            try:
                pe_ratio = float(price) / float(result)
            except ZeroDivisionError:
                pe_ratio = 0

            return True, pe_ratio
