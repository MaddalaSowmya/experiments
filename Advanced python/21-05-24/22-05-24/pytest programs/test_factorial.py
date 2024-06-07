import factorial

class Test_fact:
        def test_case1(self):
                assert factorial.factorial_func(5)==120
                print("test1")

        def test_case2(self):
                assert factorial.factorial_func(-90)==1
                print("test2")