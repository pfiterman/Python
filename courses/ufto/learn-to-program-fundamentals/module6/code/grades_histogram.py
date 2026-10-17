import tkinter.filedialog
import grades

grades_filename = tkinter.filedialog.askopenfilename()
grades_file = open(grades_filename, "r")

histogram_filename = tkinter.filedialog.askopenfilename()
histogram_file = open(histogram_filename, "w")

# Read the grades into a list
list_grades = grades.read_grades(grades_file)

# Count the grades per range
range_counts = grades.count_grade_ranges(list_grades)

# Write the histogram to the file
grades.write_histogram(range_counts, histogram_file)