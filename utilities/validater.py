stock_symbol_mapping = {
    1: "TEA",
    2: "POP",
    3: "ALE",
    4: "GIN",
    5: "JOE"
}


indicator_mapping = {
    1: "BUY",
    2: "SELL"
}


class validate_inputs():
    
    def validate(user_input, mapping_type):
        if mapping_type == "stock_symbol":
            if user_input not in stock_symbol_mapping.keys():
                return False
            else:
                return True

        if mapping_type == "indicator":
            if user_input not in indicator_mapping.keys():
                return False
            else:
                return True
