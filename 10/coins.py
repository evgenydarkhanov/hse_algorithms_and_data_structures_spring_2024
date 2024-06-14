def exchange(coins: list[int], money: int) -> list:
	result = []
	i = len(coins) - 1
	while money > 0:
		while i > -1:
			if money >= coins[i]:
				money -= coins[i]
				result.append(coins[i])
				continue
			else:
				i -= 1
				continue
		break
	if money != 0:
		return []
	return result
	
	
if __name__ == "__main__":
	print('[1, 2, 5, 10], 11 == ', exchange([1, 2, 5, 10], 11))
	print('[1, 2, 5], 11 == ', exchange([1, 2, 5], 11))
	print('[1, 2, 5, 10], 9 == ', exchange([1, 2, 5, 10], 9))
	print('[2, 5, 10], 1 == ', exchange([2, 5, 10], 1))

