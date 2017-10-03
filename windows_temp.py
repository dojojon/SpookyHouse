def read_file():
    result = []
    windows_file = open('windows_data.txt', 'r')
    window_lines = windows_file.readlines()
    for line in window_lines:
        line = line.rstrip('\n')
        line = line.split(',')
        line = {
            'x1': line[0],
            'y1': line[1],
            'x2': line[2],
            'y2': line[3]
        }
        result.append(line)
    windows_file.close()
    return result


def save_file():
    window_positions = [
        [182, 385, 	224, 472],
        [272, 385,	314, 473],
        [520, 386,	560, 470],
        [606, 385,	648, 471],

        [184, 275,	224, 348],
        [273, 275,	314, 348],
        [395, 275,	436, 345],
        [518, 275,	561, 348],
        [606, 275,	646, 348],

        [239, 179,	269, 220],
        [395, 178,	428, 220],
        [559, 178,	592, 220],

        [395, 408, 438, 478],
        [73, 428, 88, 458]]

    windows_file = open('windows_data.txt', 'w')

    for item in window_positions:
        item = str(item)
        item = item.replace('[', '')
        item = item.replace(']', '')
        windows_file.write('%s\n' % item)

    windows_file.close()


save_file()

result = read_file()

print (result)

print(result[0])
