

# 1.8 Calculating with dictionaries

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

print(prices)

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# `zip` creates an iterator that can only be consumed once
# prices_and_names = zip(prices.values(), prices.keys())
# print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError

# functions work on values not keys
print(min(prices))
print(max(prices))

# use `values`method to perform functions on values instead of keys
print(min(prices.values()))
print(max(prices.values()))

# `min` and `max` functions with key parameter
min_price = min(prices, key=lambda k: prices[k])
max_price = max(prices, key=lambda k: prices[k])
print(min_price)
print(max_price)

min_value = prices[min(prices, key=lambda k:prices[k])]
print(min_value)

# another example | using `zip`
prices = {'AAA': 45.23, 'ZZZ': 45.23}
min_tuple = min(zip(prices.values(), prices.keys()))
max_tuple = max(zip(prices.values(), prices.keys()))
print(min_tuple)
print(max_tuple)
