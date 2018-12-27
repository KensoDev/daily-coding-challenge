"""
Solution

"""


class Solution:
    def __init__(self, **kwarg):
        self.storage = dict()
        pass

    def solve(self, numbers: list, num: int) -> bool:
        result = False

        for _number in numbers:
            # What do we expect our numbers to have?
            expected = num - _number
            self.storage[_number] = num - _number

            # If we have the expected number already in storage, we can break
            if self.storage.get(expected):
                result = True
                break

        return result
