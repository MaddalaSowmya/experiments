import area

class Testareas:
        def test_pass_cases(self):
                assert area.square(2)==4
                print(f"area of square")
                assert area.triangle(4,5)==10
                print(f"area of triangle")
                assert area.rectangle(20,5)==100
                print(f"area of rectangle")

        def test_fail_cases1(self):
                assert area.square(3)==4
                print(f"area of square")
                assert area.triangle(4,5)==10
                print(f"area of triangle")
                assert area.rectangle(20,5)==100
                print(f"area of rectangle")

        def test_fail_cases2(self):
                assert area.triangle(4,5)==10
                print(f"area of triangle")
                assert area.square(3)==4
                print(f"area of square")
                assert area.rectangle(20,5)==100
                print(f"area of rectangle")
