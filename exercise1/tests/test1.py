from IPython.display import display, Markdown
import time
test_cases1 = [
    {"input": 1, "expected_output": 1},
    {"input": 33, "expected_output": 6},
    {"input": 22, "expected_output": 4},
    {"input": 123, "expected_output": 6},
    {"input": 45, "expected_output":9}
]


def test_code_1(func):
    passed = 0
    for i, test_case in enumerate(test_cases1):
        time.sleep(2)
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        try:
            user_result = func(input_data)
            if user_result == expected_output:
                passed += 1
                print(f"Test case {i+1}: Passed")
            else:
                print(f"Test case {i+1}: Failed - Expected {expected_output}, but got {user_result}")
        except Exception as e:
            print(f"Test case {i+1}: Error occurred - {e}")
    if len(test_cases1) == passed:
        display(Markdown("## Congratulations! You passed all the test cases!"))
    else:
        display(Markdown("## Hey.. Don't worry. Youre almost there. Try again!"))
    

def test_code_2(func):
    test_cases2 = [
        {"input": 1.49, "expected_output": (1,0.49)},
        {"input": 2, "expected_output":(2,0) },
        {"input": 3.33, "expected_output": (3,0.33)},
        {"input": 12.3, "expected_output": (12,0.3)},
        {"input": 0.45, "expected_output":(0,0.45)}
    ]
    passed = 0
    for i, test_case in enumerate(test_cases2):
        time.sleep(2)
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        try:
            a,b = func(input_data)
            if b!=0:
                b = float(f'{b:.2f}')
            user_result = a,b
            if user_result == expected_output:
                passed += 1
                print(f"Test case {i+1}: Passed")
            else:
                print(f"Test case {i+1}: Failed - Expected {expected_output}, but got {user_result}")
        except Exception as e:
            print(f"Test case {i+1}: Error occurred - {e}")
    if len(test_cases2) == passed:
        display(Markdown("## Congratulations! You passed all the test cases!"))
    else:
        display(Markdown("## Hey.. Don't worry. Youre almost there. Try again!"))
    
    
def test_code_3(func):
    test_cases3 = [
        {"input": 123, "expected_output": 14},
        {"input": 246, "expected_output": 56},
        {"input": 333, "expected_output": 27},
        {"input": 12, "expected_output": 5},
        {"input": 9, "expected_output": 81}
    ]
    passed = 0
    for i, test_case in enumerate(test_cases3):
        time.sleep(2)
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        try:
            user_result = func(input_data)
            if user_result == expected_output:
                passed += 1
                print(f"Test case {i+1}: Passed")
            else:
                print(f"Test case {i+1}: Failed - Expected {expected_output}, but got {user_result}")
        except Exception as e:
            print(f"Test case {i+1}: Error occurred - {e}")
    if len(test_cases3) == passed:
        display(Markdown("## Congratulations! You passed all the test cases!"))
    else:
        display(Markdown("## Hey.. Don't worry. Youre almost there. Try again!"))



def test_code_practice(func):
    test_cases3 = [
        {"input1": 3, "input2":2 ,"expected_output": 11},
        {"input1": 1, "input2":2,"expected_output":5 },
    ]
    passed = 0
    for i, test_case in enumerate(test_cases3):
        time.sleep(2)
        input_data_1 = test_case["input1"]
        input_data_2 = test_case["input2"]
        expected_output = test_case["expected_output"]
        try:
            user_result = func(input_data_1,input_data_2)
            if user_result == expected_output:
                passed += 1
                print(f"Test case {i+1}: Passed")
            else:
                print(f"Test case {i+1}: Failed - Expected {expected_output}, but got {user_result}")
        except Exception as e:
            print(f"Test case {i+1}: Error occurred - {e}")
    if len(test_cases3) == passed:
        display(Markdown("## Congratulations! You passed all the test cases!"))
    else:
        display(Markdown("## Hey.. Don't worry. Youre almost there. Try again!"))

    
    
