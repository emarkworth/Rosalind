
infile = '/Users/elimarkworth/Downloads/rosalind_ini5.txt'

output_list = []


with open(infile, 'r') as file:
    for line in file:
        line.strip()
        output_list.append(line)

counter = 0
with open('wwf_output.txt', 'w') as outfile:

    for line in output_list:
        counter += 1
        if counter % 2 != 0:

            try:
                outfile.write(output_list[counter])
            except IndexError:
                print("List end")


