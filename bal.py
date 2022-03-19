import pyupbit


access = ""
secret = ""

upbit = pyupbit.Upbit(access, secret)
balance = upbit.get_balance("KRW")
print(balance)
