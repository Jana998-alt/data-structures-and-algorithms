from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import validate_brackets





def test_case_one():
  actual =  True
  expected = validate_brackets('{}')
  assert actual == expected


def test_case_2():
  actual =  True
  expected = validate_brackets('{}(){}')
  assert actual == expected


def test_case_3():
  actual =  True
  expected = validate_brackets('()[[Extra Characters]]')
  assert actual == expected


def test_case_4():
  actual =  True
  expected = validate_brackets('(){}[[]]')
  assert actual == expected


def test_case_5():
  actual =  True
  expected = validate_brackets('{}{Code}[Fellows](())')
  assert actual == expected


def test_case_6():
  actual =  False
  expected = validate_brackets('[({}]')
  assert actual == expected


def test_case_6():
  actual =  False
  expected = validate_brackets('[({}]')
  assert actual == expected


def test_case_7():
  actual =  False
  expected = validate_brackets('(](')
  assert actual == expected


def test_case_8():
  actual =  False
  expected = validate_brackets('{(})')
  assert actual == expected

def test_case_8():
  actual =  False
  expected = validate_brackets('}')
  assert actual == expected

def test_case_9():
  actual =  False
  expected = validate_brackets(')')
  assert actual == expected

def test_case_10():
  actual =  False
  expected = validate_brackets('{]')
  assert actual == expected

def test_version():
    assert __version__ == '0.1.0'
