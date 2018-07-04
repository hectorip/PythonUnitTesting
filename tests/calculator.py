
# Test Driven Development

# Prueba -> Código -> Refactoring

class Calculator():

    def get_iva(self, price, rate=0.16):
        return price * rate

    def calculate_interest(self, initial_amount, rate, periods, compound=False):
        if compound:
            result = 0
            
            for i in range(0, periods):
                result += initial_amount * rate
                initial_amount += initial_amount * rate
            
            return round(result, 2)
        else:
            return initial_amount * rate * periods
