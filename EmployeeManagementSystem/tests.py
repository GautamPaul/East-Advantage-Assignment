import unittest
from ems import Employee, add_employee

class TestEMS(unittest.TestCase):
    def test_employee_class(self):
        e = Employee(name="emp1", id=1, title="tit1", department="dep1")
        self.assertEqual(e.__str__(), "emp1 1")

    # def test_add_employee(self):
    #     add_employee()

if __name__ == '__main__':
    unittest.main()