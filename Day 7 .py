def manual_sort(numbers):
   
    for i in range(len(numbers)):
        min_idx = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


def analyze_list(numbers):
  
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    
    for i in range(len(numbers)):
        total += numbers[i]
        if numbers[i] < minimum:
            minimum = numbers[i]
        if numbers[i] > maximum:
            maximum = numbers[i]
    
    average = total / len(numbers)
    
    return {
        "Sorted List": numbers,
        "Sum": total,
        "Average": average,
        "Minimum": minimum,
        "Maximum": maximum
    }


def print_analysis(results):
    print("\n📊 Summary of Statistics:")
    for idx, (key, value) in enumerate(results.items(), start=1):
        print(f"{idx}. {key}: {value}")


def get_valid_input():
    while True:
        user_input = input("🔢 Enter numbers separated by commas: ")
        try:
            numbers = [int(x.strip()) for x in user_input.split(",")]
            if len(numbers) == 0:
                print("⚠️ Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("❌ Invalid input. Please enter only integers separated by commas.")


if __name__ == "__main__":
    print("📘 Smart List Analyzer – Day 7")
    
    nums = get_valid_input()
    sorted_nums = manual_sort(nums.copy())  
    stats = analyze_list(sorted_nums)
    print_analysis(stats)
