import pytest

@pytest.mark.parametrize("input1,input2,exp_op",
                         [
                             (0,0,0),
                             (1,2,3),
                             (-1,1,0),
                             ('hi','everyone','hieveryone')
                         ])

def test_add(input1,input2,exp_op):
    assert input1+input2==exp_op

@pytest.mark.parametrize("input,exp_op",
                         [
                             (0, 0),
                             (2, 4),
                             (-1, 1),
                             (1, 1)
                         ])
def test_square(input, exp_op):
    assert input*input == exp_op

@pytest.mark.parametrize("input,exp_op",
                         [
                             ('Gowri', 'owri'),
                             ('Good morning', 'ood mornin'),
                             ('I am going', 'I am oin'),
                             ('oggy and the cockroaches', 'oy and the cockroaches'),
                             ('Goodday biscuits are good', 'oodday biscuits are ood')
                         ])
def test_remove_g_from_string(input, exp_op):
    str = input.replace('g','').replace('G','')
    assert str == exp_op
