import calculator

class TestCalculator:
    def test_multiple(self):
        assert 4 == calculator.multiple(2,2)
    def test_divide(self):
        assert 4 == calculator.divide(8,2)
        
