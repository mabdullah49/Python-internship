def calculate_gpa(grades, weights=None):
   
    if not grades:
        return 0.0

    if weights is None:
        weights = [1] * len(grades)  

    if len(grades) != len(weights):
        raise ValueError("Grades and weights must be the same length.")

    weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
    total_weight = sum(weights)

    gpa = weighted_sum / total_weight
    return round(gpa, 2)


def display_gpa(name, grades, weights=None):
    """
    Display GPA using a formatted print statement.
    """
    gpa = calculate_gpa(grades=grades, weights=weights) 
    print(f"{name}'s GPA is: {gpa}")



grades_list = [3.8, 3.6, 4.0, 3.9]
weights_list = [3, 3, 4, 2]  

display_gpa(name="Alice", grades=grades_list, weights=weights_list)
display_gpa(name="Bob", grades=[3.0, 3.5, 4.0])  
