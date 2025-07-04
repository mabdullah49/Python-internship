def read_student_marks(file_path):
    student_marks = {}
    skipped_entries = 0

    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    name, mark = line.strip().split(',')
                    name = name.strip()
                    mark = mark.strip()

                    if not name or not mark:
                        raise ValueError(f"Missing data on line {line_num}")

                    mark = int(mark)
                    student_marks[name] = mark

                except ValueError as ve:
                    print(f"Skipped line {line_num}: {ve}")
                    skipped_entries += 1

    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please check the path.")

    return student_marks, skipped_entries


def display_marks_summary(student_marks):
    print("\n📋 Student Marks:")
    if not student_marks:
        print("No valid data available to display.")
        return

    total = 0
    for name, mark in student_marks.items():
        print(f"{name}: {mark}")
        total += mark

    try:
        average = total / len(student_marks)
        print(f"\n📊 Average Mark: {average:.2f}")
    except ZeroDivisionError:
        print("Cannot calculate average: No valid entries.")


def main():
    while True:
        file_path = input("Enter the path to the marks file: ")

        try:
            student_marks, skipped = read_student_marks(file_path)
            display_marks_summary(student_marks)
            print(f"\n⚠️ Skipped entries: {skipped}")
            break
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            print("Please try again.\n")


if __name__ == "__main__":
    main()
