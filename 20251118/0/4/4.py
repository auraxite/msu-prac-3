with open('ru_in.txt', 'rb') as file_in:
    data = file_in.read()
    with open('ru_out.txt', 'wb') as file_out:
        file_out.write(data[len(data) // 2:] + data[:len(data) // 2])