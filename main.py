from currency_crypto import Currency_crypto

crypto = Currency_crypto('51d9e71e0964d685114b0bb3296147c2c10ba27bab4dd6ab7b5675726fc0')
print(crypto.cryptocurrency_data(1)) # вызов данных монеты по ее id
print(crypto.cryptocurrency_list()) # вызов всех id монет
print(crypto.currency_data()) # Курс USD к RUB                                                                              