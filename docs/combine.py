import sys

def merge_files(input_file1, input_file2, output_file):
  with open(input_file1, "r") as f1:
    lines1 = f1.readlines()

  with open(input_file2, "r") as f2:
    lines2 = f2.readlines()

  lines = sorted(lines1 + lines2)

  with open(output_file, "w") as f:
    for line in lines:
      f.write(line)

if __name__ == "__main__":
  if len(sys.argv) != 4:
    print("Usage: python merge_files.py input_file1 input_file2 output_file")
    exit(1)

  input_file1 = sys.argv[1]
  input_file2 = sys.argv[2]
  output_file = sys.argv[3]

  merge_files(input_file1, input_file2, output_file)
