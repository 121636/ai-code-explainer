from main import explain_code

if __name__ == "__main__":
    sample_code = "def add(a, b): return a + b"
    result = explain_code(sample_code)
    print(result)
