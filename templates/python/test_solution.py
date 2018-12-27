"""
Solution Testing

"""

from hamcrest import (
    assert_that,
    empty,
    has_length,
    has_entries,
    is_,
)

from solution import Solution


def test_solution():
    solution = Solution()
