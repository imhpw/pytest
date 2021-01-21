import pytest
import yaml
from python.calc import Calc

class YamlData:
    def __init__(self,path):
        with open(path) as f:
            self.data= yaml.safe_load(f)
    def get_data(self,name):
        return self.data[name]


add_data = YamlData('./dates/calcdata.yaml')


class TestCalc:
    @pytest.fixture()
    def db(self):
        self.calc = Calc()
    # def setup(self):
    #     self.calc = Calc()

    @pytest.mark.parametrize('test_date',add_data.get_data('norm'))
    def test_add_1(self,db, test_date):
        result = self.calc.add(test_date['a'], test_date['b'])
        print(result)
        assert test_date['c'] == result

    @pytest.mark.parametrize('test_date', add_data.get_data('except'))
    def test_add_2(self, db, test_date):
        with pytest.raises(TypeError):
            self.calc.add(test_date['a'], test_date['b'])

    @pytest.mark.finished
    @pytest.mark.parametrize('a,b,c',
                             [(2, 1, 2), (-1, 1, -1), (999, 1, 999), (-1, -2, 0.5), (0.1, 0.1, 1), (-0.1, 1, -0.1)])
    def test_div(self,db,a,b,c):
        result = self.calc.div(a, b)
        print(result)
        assert c == result


if __name__ == '__main__':
    pytest.main(['-sv', 'test_demo.py'])
