def fibonacci(n):
    fib_seq = [0, 1]
    
    for i in range(2, n):
        next_term = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_term)
    
    return fib_seq[:n]

try:
    n_terms = int(input("Enter the number of terms: "))
    
    if n_terms <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = fibonacci(n_terms)
        print(f"Fibonacci sequence up to {n_terms} terms: {fibonacci_sequence}")
except ValueError:
    print("Please enter a valid integer.")
