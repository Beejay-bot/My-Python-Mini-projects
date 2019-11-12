shirt_price = 200
jeans_price = 250
native_attire_price = 200
tshirt_price  = 200
stockings_price = 150

shirt = input('how many shirts washed ? :')
jeans = input('how many jeans washed? :')
native_attire = input('how native attires washed? :')
tshirt = input('how many tshirt washed? :')
stockings = input ('how many stockings washed? :')


shirt_statement = 'You washed' ' ' + shirt + ' ' 'shirt. And'
jeans_statement = 'You washed' ' ' + jeans + ' ' 'shirt.'
native_attire_statement = 'You also washed' ' ' + native_attire + ' ' 'native_attire.'
tshirt_statement = 'Also, You washed' ' ' + tshirt + ' ' 'tshirt.'
stockings_statement = 'And, You washed' ' ' + stockings + ' ' 'stockings.' 
cloths_washed = "The amount of clothes you've is " + str(int(shirt) + int(jeans) + int(native_attire) + int(tshirt) + int(stockings) )
amount_to_be_payed = "your bill is  " + str( shirt_price * int(shirt) + jeans_price * int(jeans) + native_attire_price *  int(native_attire ) + tshirt_price * int(tshirt) + stockings * int(stockings))
print(cloths_washed)
print(shirt_statement, jeans_statement , native_attire_statement ,tshirt_statement , stockings_statement  ) 
print(amount_to_be_payed)
print('Thank you for  patronising us.')