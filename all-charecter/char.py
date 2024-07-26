# Normal characters
with open('all-chars.txt', 'w') as f:
    for number in range(0, 128):  # Range modified to include 0-127
        f.write(chr(number) + "\n")

# URL-encoded characters
with open('url-encoded-chars.txt', 'w') as f:
    for number in range(0, 128):  # Range modified to include 0-127
        # Convert to URL-encoded format
        encoded_char = '%' + format(number, '02X')
        f.write(encoded_char + "\n")
