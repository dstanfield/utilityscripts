from pathlib import Path, PureWindowsPath

filenamedouble = PureWindowsPath("source_data\\text_files\\raw_data.txt")
filenamesingle = PureWindowsPath("source_data\text_files\raw_data.txt")
filenamewhatever = "source_data\text_files\raw_data.txt"

# Convert path to the right format for the current operating system
correctdouble = Path(filenamedouble)
correctsingle = Path(filenamesingle)
whatever = Path("r" +  filenamewhatever)

print(correctdouble)
print(correctsingle)
print(filenamewhatever)