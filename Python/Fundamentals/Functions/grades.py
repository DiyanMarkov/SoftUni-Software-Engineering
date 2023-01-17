def grades(grade):
    """This function gives output on student grades"""
    result = None
    if grade >= 2 and grade < 3:
        result = "Fail"
    elif grade < 3.50:
        result = "Poor"
    elif grade < 4.50:
        result = "Good"
    elif grade < 5.50:
        result = "Very Good"
    else:
        result = "Excellent"

    return result


score = float(input())
print(grades(score))