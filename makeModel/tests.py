import unittest
import tools

class TestStringMethods(unittest.TestCase):

    # Check list + list -> List of Dicts conversion
    def test_inputconversion(self):
        a = ['M1', 'M2', 'MUE']
        b = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [4, 5, 6]]
        c = [{'M1' : 1, 'M2' : 2, 'MUE' : 3}, {'M1' : 1, 'M2' : 2, 'MUE' : 3},
             {'M1' : 1, 'M2' : 2, 'MUE' : 3}, {'M1' : 4, 'M2' : 5, 'MUE' : 6}]
        self.assertEqual(c, tools.convertInput(a, b))

    def test_writeFH(self):
        newParams = {'MT': -1000, 'M3SQ' : 1500, 'M3SU' : 1500, 'M3SD' : 1500,
              'M3SL' : 500, 'M3SE' : 500, 'Abs(Xt)' : 3675, 'M2SQ' : 1500,
              'M2SU' : 1500, 'M2SD' : 1500, 'M2SL' : 500, 'M2SE' : 500,
              'M1SQ' : 1500, 'M1SU' : -1000, 'M1SD' : 1500, 'M1SL' : 500,
              'M1SE' : 500, 'Abs(Ac)' : 0, 'Abs(As)' : 0, 'Abs(Amu)' : 0,
              'Abs(M_3)' : -1000, 'Abs(M_2)' : 200, 'Abs(MUE)' : 2000}

        tempParams = tools.writeFH({'MT' : -1000, 'M1SU' : -1000, 'Abs(M_3)' : -1000})
        self.assertEquals(newParams, tempParams)

if __name__ == '__main__':
    unittest.main()