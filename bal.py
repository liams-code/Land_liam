import pyupbit


access = "pnOxTRGv2r6Ogmto3GP9rSOUvzGgVBPymlgxkHMM"
secret = "xYkxvaEj2P6T3r6NtCiH8Rg5oJdAaQRNxQ92xF5s"

upbit = pyupbit.Upbit(access, secret)
balance = upbit.get_balance("KRW")
print(balance)
