apples = {
    'pink lady': 17,
          'braeburn': 21,
          'royal gala': 12,
          'empire': 22,
          'mutsu': 19
}

mutsu_stock = apples['mutsu']
print('We have ' + str(mutsu_stock) + ' ' + 'mutsu apples.')

for apple in apples.keys():
    print(apple)

for apple, stock_count in apples.items():
    print( 'We have' + ' ' + str(stock_count) + ' ' + apple + ' ' + 'apples')

mac_apples = apples.get('macintosh', 3)
print(mac_apples)