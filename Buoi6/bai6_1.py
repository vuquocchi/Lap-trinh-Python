# Bài tập 6.1 - Giai thừa bằng đệ quy

def giai_thua_de_quy(n):
    # Điều kiện dừng
    if n <= 1:
        return 1

    # Gọi lại chính hàm đó
    return n * giai_thua_de_quy(n - 1)


# Giai thừa bằng vòng lặp
def giai_thua_lap(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua


# Gọi hai hàm
print(giai_thua_de_quy(5), "-", giai_thua_lap(5))