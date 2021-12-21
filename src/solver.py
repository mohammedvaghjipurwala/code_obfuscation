
class Solver:
    def solve(self, equation):
        try:
            result = eval(equation['equation'])
            result = 'Valid Equation and result is ' + str(result)
        except Exception:
            result = 'Invalid Equation'
        return result
