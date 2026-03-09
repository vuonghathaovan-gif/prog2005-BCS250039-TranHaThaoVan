
so_le = [i for i in range(111, 16, -1) if i % 2 != 0]
print(so_le)
print()
def kiem_tra(n):
  if n > 1:
    return not any(n % i == 0 for i in range(2, int(n**0.5) + 1))
  else:
    return False

so_nguyen_to = [num for num in range(17, 112) if kiem_tra(num)]
print(*so_nguyen_to)







