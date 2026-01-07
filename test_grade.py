from students import calculate_grade

def test_grades():
    assert calculate_grade(95) == "S"
    assert calculate_grade(85) == "A"
    assert calculate_grade(70) == "B"
    assert calculate_grade(55) == "C"
    assert calculate_grade(45) == "D"
    assert calculate_grade(30) == "F"
