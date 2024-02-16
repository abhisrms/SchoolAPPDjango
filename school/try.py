import pandas as pd
import random

# Sample data
first_names = ['John', 'Emma', 'Michael', 'Sophia', 'James', 'Olivia', 'William', 'Ava', 'Alexander', 'Isabella']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
usernames = ['user' + str(i) for i in range(1, 51)]
passwords = [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=8)) for _ in range(50)]
rolls = [random.randint(100, 999) for _ in range(50)]
mobiles = [''.join(random.choices('1234567890', k=10)) for _ in range(50)]
fees = [random.randint(5000, 10000) for _ in range(50)]
classes = ['Class' + str(random.randint(1, 5)) for _ in range(50)]
statuses = [random.choice([True, False]) for _ in range(50)]

# Create DataFrame
data = {
    'First Name': random.choices(first_names, k=50),
    'Last Name': random.choices(last_names, k=50),
    'Username': usernames,
    'Password': passwords,
    'Roll': rolls,
    'Mobile': mobiles,
    'Fee': fees,
    'Class': classes,
    'Status': statuses
}

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('sample_data.csv', index=False)