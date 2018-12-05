available_apples = ['cox', 'pink lady', 'braeburn']
available_apples.append('royal gala')

print(available_apples)

# append means to add

available_apples.remove('cox')

new_apples = ['pink ladies', 'empire', 'mutsu', 'rasberry','royal gala']
available_apples.extend(new_apples)

print(available_apples)

unique_apples = set(available_apples)


available_apples = list(unique_apples)
print(available_apples)