import csv

def build_profession_set(filename):
    profession_set = set()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            profession = row[1].strip().lower()
            if profession not in {'student', 'unemployed', 'housemaid'}:
                profession_set.add(profession)
    return profession_set

def is_eligible(age, profession):
    low_income_professions = {'student', 'unemployed'}
    return 20 <= age <= 50 and profession not in low_income_professions

def compute_age_limits(filename):
    min_age = float('inf')
    max_age = float('-inf')
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            age = int(row[0])
            min_age = min(min_age, age)
            max_age = max(max_age, age)
    return {'min': min_age, 'max': max_age}

def main():
    filename = 'bank-data.csv'
    profession_set = build_profession_set(filename)
    age_limits = compute_age_limits(filename)

    while True:
        profession = input("Enter the profession of the client (or 'END' to quit): ").strip().lower()

        if profession == 'end':
            break

        age = int(input("Enter the age of the client: "))
        
        if profession in profession_set and is_eligible(age, profession):
            print("Client is eligible for the marketing campaign.")
        else:
            print("Client is not eligible for the marketing campaign.")

    print(f"Minimum eligible age: {age_limits['min']}")
    print(f"Maximum eligible age: {age_limits['max']}")

if __name__ == "__main__":
    main()
