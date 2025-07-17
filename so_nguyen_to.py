n = int(input("Nhập số nguyên: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print("Là số nguyên tố" if is_prime else "Không phải số nguyên tố")
