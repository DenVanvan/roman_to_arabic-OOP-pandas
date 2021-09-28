
class RomanInt:


    def __init__(self, roman):
        self.integer = 0
        fig = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for string in roman:
            if roman.index(string) != len(roman)-1 and fig[roman[roman.index(string)]] < fig[roman[roman.index(string)+1]]:
                self.integer = self.integer - fig[roman[roman.index(string)]]

            else:
                self.integer = self.integer + fig[roman[roman.index(string)]]

        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        self.result = ''
        int_2 = self.integer
        while int_2 > 0:
            if int_2 >= value[i]:
                int_2 = int_2 - value[i]
                self.result = self.result + symbol[i]
            else:
                i += 1


