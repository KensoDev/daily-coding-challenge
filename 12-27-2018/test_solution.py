"""
Solution Testing

"""

from hamcrest import (
    assert_that,
    is_,
)
from parameterized import parameterized

from solution import Solution


@parameterized([
    ([10, 15, 3, 7], 17, True),
    ([10, 15, 3, 8], 17, False),
])
def test_solution(numbers, result, expected):
    solution = Solution()
    assert_that(solution.solve(numbers, result), is_(expected))
