# Given a list of mixed data types, categorize them by type and count occurrences.
from collections import Counter

data = [1, "hello", 3.14, True, [1,2,3], None, {"key": "value"}, (1,2)]
type_list = []

for element in data:

    element_type = type(element).__name__
    print(element_type)
    type_list.append(element_type)

print(Counter(type_list))