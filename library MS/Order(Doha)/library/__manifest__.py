
import random
import pandas as pd

# Function to generate random data
def generate_random_data(num_rows):
    data = []
    for i in range(1, num_rows + 1):
        link_image = f"https://example.com/image_{i}.jpg"
        name = f"Author {i}"
        address = f"Address {i}"
        author_id = i
        email = f"author{i}@example.com"
        phone_number = f"123-456-{i:04d}"
        birthdate = f"2000-01-{i:02d}"
        active = random.choice([True, False])
        data.append([link_image, name, address, author_id, email, phone_number, birthdate, active])

    return data

# Generate random data
num_rows = 20
data = generate_random_data(num_rows)

# Create a DataFrame
columns = ['Link Image', 'Name', 'Address', 'Author ID', 'Emails', 'Phone Number', 'Birthdate', 'Active']
df = pd.DataFrame(data, columns=columns)

# Save DataFrame as CSV
df.to_csv('author_dataset.csv', index=False)