import traceback

# Task 1: Diary
try:
    with open("diary.txt", "a") as file:
        line = input("What happened today? ")
        file.write(line + "\n")
        while line != "done for now":
            line = input("What else? ")
            file.write(line + "\n")

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")