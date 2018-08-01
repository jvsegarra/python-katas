class FizzBuzz(object):

    def fizz_buzz(self, input_list):
        result = []
        for number in input_list:
            if number % 5 == 0 and number % 3 == 0:
                result += ["FizzBuzz"]
            elif number % 3 == 0:
                result += ["Fizz"]
            elif number % 5 == 0:
                result += ["Buzz"]
            else:
                result += [str(number)]

        return result
