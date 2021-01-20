import pytest
from python.calc import Calc


class TestCalc:

    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1,3)
        print(result)
        assert 4 == result

    def test_div(self):
        self.calc = Calc()
        result = self.calc.div(2,2)
        assert 1 == result

if __name__ == '__main__':
    pytest.main(['-v', 'test_demo.py::TestCalc'])
