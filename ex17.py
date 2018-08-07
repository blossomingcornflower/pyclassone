from sys import argv
from os.path import exists

script, form_file, to_file = argv

print(f"Copying from {form_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(form_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()