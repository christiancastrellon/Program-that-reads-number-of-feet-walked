# Define your function here 
def feet_to_steps(user_feet):
    return int(user_feet/2.5)
if __name__ == '__main__':
    # Type your code here.
    input_feet = float(input())
    steps_walked = feet_to_steps(input_feet)
    print(steps_walked)