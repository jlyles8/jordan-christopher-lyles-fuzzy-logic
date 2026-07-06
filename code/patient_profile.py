import random
import csv

# Define the ranges for each category
age_ranges = [(0, 2), (3, 8), (9, 14), (15, 21), (22, 35), (36, 65), (65, 100)]
bmi_ranges = [(15, 18), (19, 24), (25, 29), (30, 34), (35, 50)]
genders = ["Female", "Male"]
races = ["Caucasian", "African American", "Hispanic", "Asian", "Native American"]
pain_durations = [(1, 7), (8, 14), (15, 21), (22, 28), (29, 35), (36, 42)]
pain_severity = list(range(1, 11))
sleep_hours = [(4, 6), (6, 8), (8, 10)]
workout_days = [(1, 7)]
water_intake = [(0, 30), (31, 64), (65, 100)]
smoking_days = [(1, 7)]
eating_frequency = [(1, 4)]
caffeine_intake = [(0, 90), (91, 200), (201, 300), (301, 400)]

# Generate 100 random datasets
num_datasets = 100
datasets = []

for _ in range(num_datasets):
    data = {
        "Age": random.randint(*random.choice(age_ranges)),
        "BMI": random.randint(*random.choice(bmi_ranges)),
        "Gender": random.choice(genders),
        "Race": random.choice(races),
        "Physical Pain - Duration": random.randint(*random.choice(pain_durations)), 
        "Physical Pain - Severity": random.choice(pain_severity), 
    
        "Sleep Habits - Hours Per Day": random.randint(*random.choice(sleep_hours)),
      
        "Lifestyle - Workout Days per Week" : random.randint(*random.choice(workout_days)),
        "Lifestyle - Water Intake (ounces)" : random.randint(*random.choice(water_intake)),
        "Lifestyle - Smoking Days per Week" : random.randint(*random.choice(smoking_days)), 
        "Lifestyle - Eating Frequency per Day" : random.randint(*random.choice(eating_frequency)),
        "Lifestyle - Caffeine Intake (mg)" : random.randint(*random.choice(caffeine_intake))       
        }

    datasets.append(data)

# Save directory
output_directory = r"C:\Users\lyles\Desktop\Outputs"
csv_filename = "random_datasets.csv"
full_path = output_directory + "\\" + csv_filename

# Write the datasets to a CSV file
with open(full_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=datasets[0].keys())

    writer.writeheader()
    for data in datasets:
        writer.writerow(data)

print(f"Data has been saved to {full_path}")
