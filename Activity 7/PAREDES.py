Job = input("IT, ACC, or HR?: ").upper()
Years = int(input("How many years have you worked?: "))

pay_tiers = {
    "IT": [(0, 5000), (5, 7000), (10, 10000), (15, 13000)],
    "ACC": [(0, 6000), (5, 8000), (10, 12000), (15, 16000)],
    "HR": [(0, 7500), (5, 9500), (10, 15000), (15, 20000)],
}

try:
    tiers = pay_tiers[Job]
    Pay = 0
    for years_threshold, pay_amount in tiers:
        if Years > years_threshold:
            Pay = pay_amount
        else:
            break  # Exit loop once the appropriate tier is found
    print(Pay)
except KeyError:
    print("Invalid job title entered.")
