from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 8
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 4
        assert result == expected

    def test_multply(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 12
        assert result == expected

    def test_divide(self):
        # arrange
        a = 6
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 3
        assert result == expected