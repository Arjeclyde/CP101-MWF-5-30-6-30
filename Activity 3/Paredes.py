hrs = input("Enter Hours")
h = float(hrs)
rate = input("Enter the Rate: ")
ra = float(rate)
if h <= 40:
    print(h * ra)
elif h > 40:
    print(40* ra + (h-40)*1.5*ra)
