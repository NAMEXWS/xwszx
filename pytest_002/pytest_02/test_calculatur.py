# import pytest
#
# from pytest_002.pytest_02.calculatur import Calculatur
#
#
# def test_add():
#     assert Calculatur().add(5, 4) == 9
#
#
# class Test_Calculatur:
#     def setup_class(self):
#         self.c = Calculatur()
#
#     @pytest.mark.smoke
#     def test_add(self):
#         result = self.c.test_add(5, 4)
#         print(result)
#         assert result == 9
#
#     def test_sub(self):
#         result = self.c.test_sub(5, 4)
#         print(result)
#         assert result == 1
#
#     def test_mul(self):
#         result = self.c.test_mul(5, 4)
#         print(result)
#         assert result == 20
#
#     def test_div(self):
#         result =self.c.test_div(20, 5)
#         print(result)
#         assert result == 4
# # if __name__ == '__main__':
# #     print(Calculatur().add(5,4))
