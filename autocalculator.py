import calculator

class TestCal:
    def test_multiple(self):
        assert 4 == calculator.multiple(2,2)
    def test_divid(self):
        assert 4 == calculator.divide(8,2)
        