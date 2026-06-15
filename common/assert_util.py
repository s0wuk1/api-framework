class AssertUtil:
    @staticmethod
    def assert_equal(actual, expected, msg=""):
        assert actual == expected, \
            f"{msg}，实际值:{actual}，期望值:{expected}"

    @staticmethod
    def assert_true(value, msg=""):
        assert value, msg

    @staticmethod
    def assert_false(value, msg=""):
        assert not value, msg


assert_util = AssertUtil()