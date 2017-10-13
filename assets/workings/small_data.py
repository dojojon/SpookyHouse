result = []

in_path = "assets/"
out_path = "assets_low/"

# open up the file for reading
windows_file = open(in_path + "ghost_data.txt", "r")
# read the contents
window_lines = windows_file.readlines()
# process each line to a list
for line in window_lines:
    line = line.rstrip("\n")
    line = line.split(",")
    # create a dictionary for each line
    line = {
        "x1": int(line[0]),
        "y1": int(line[1]),
        "x2": int(line[2]),
        "y2": int(line[3]),
        "visible": False
    }
    # add to a list
    result.append(line)
# close the file
windows_file.close()

windows_file = open(out_path + "ghost_data.txt", "w")
fact = 0.8
for line in result:
    dump_line =  str(int(line["x1"] * fact)) + "," + str(int(line["y1"] * fact)) + \
        "," + str(int(line["x2"] * fact)) + "," + \
        str(int(line["y2"] * fact)) + "\n"
    print(dump_line)
    windows_file.write(dump_line)
windows_file.close()
