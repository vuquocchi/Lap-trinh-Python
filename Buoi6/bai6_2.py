# Bài tập 6.2 - Fibonacci bằng đệ quy

def fibonacci_de_quy(n):
    # Điều kiện dừng
    if n <= 1:
        return n

    # Gọi lại chính hàm
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


# In 10 số Fibonacci đầu tiên
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")

print()