class Solution(object):
    def reverse(self, x):
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        result = 0

        while x != 0:
            digit = x % 10  # fetch last digit
            x = x // 10     # remove last digit

            if sign == 1:
                if result > 214748364:
                    return 0
                elif result == 214748364 and digit > 7:
                    return 0
            else:
                if result > 214748364:
                    return 0
                elif result == 214748364 and digit > 8:
                    return 0

            result = result * 10 + digit

        return result * sign
