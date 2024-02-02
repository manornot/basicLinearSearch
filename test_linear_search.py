import subprocess

def run_test(array_size, array_elements, target, expected_output):
    # Prepare the input
    input_text = f"{array_size}\n{' '.join(map(str, array_elements))}\n{target}\n"
    # Run the compiled program, feeding it the input text
    process = subprocess.run(['./linear_search'], input=input_text, capture_output=True, text=True, stdin=subprocess.PIPE)
    output = process.stdout.strip()
    # Assert to check if the actual output contains the expected result
    assert expected_output in output, f"Test failed for input '{input_text}'. Expected to find '{expected_output}' in output, got '{output}'"

def compile_program():
    # Compile the C program to a binary named 'linear_search'
    compile_process = subprocess.run(['gcc', 'linear_search.c', '-o', 'linear_search'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        print("Compilation failed.")
        print(compile_process.stderr)
        exit(1)

def main():
    compile_program()
    # Define a list of test cases
    test_cases = [
        (5, [1, 2, 3, 4, 5], 3, "Number found at index: 2"),
        (4, [7, 8, 9, 10], 5, "Number not found in the array"),
        (3, [15, 25, 35], 35, "Number found at index: 2"),
    ]
    # Run tests for each case
    for size, elements, target, expected in test_cases:
        run_test(size, elements, target, expected)
    
    print("All tests passed successfully.")

if __name__ == "__main__":
    main()
