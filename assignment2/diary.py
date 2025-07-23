#Task 1

import traceback

try:
    with open("diary.txt", "a") as diary_file:
        prompt = "What happened today? "

        while True:
            diary_input = input(prompt)
            diary_file.write(diary_input + "\n")

            if diary_input.lower().strip() == "done for now":
                break
            prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
