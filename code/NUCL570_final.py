import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import random
import matplotlib.pyplot as plt

# Define medication data
medication_data = {
    "Acetaminophen (Tylenol)": {"Ease of Use Score": 90, "Cost Score": 80, "Accessibility Score": 85, "Pain Treatment Score": 95, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Lower Back", "Headaches and Migraines"]},
    "Ibuprofen (Advil)": {"Ease of Use Score": 85, "Cost Score": 85, "Accessibility Score": 80, "Pain Treatment Score": 90, "Adverse Effects Score": 75, "Duration Score": 80, "Affected Body Parts": ["Neck and Shoulder", "Knee and Joint"]},
    "Naproxen (Aleve)": {"Ease of Use Score": 80, "Cost Score": 85, "Accessibility Score": 75, "Pain Treatment Score": 90, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Knee and Joint", "Headaches and Migraines"]},
    "Aspirin (Bayer)": {"Ease of Use Score": 80, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 85, "Adverse Effects Score": 75, "Duration Score": 85, "Affected Body Parts": ["General Pain", "Backaches", "Muscle Pain", "Headaches and Migraines"]},
    "Diclofenac (Voltaren)": {"Ease of Use Score": 75, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 85, "Adverse Effects Score": 80, "Duration Score": 75, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Knee and Joint", "Headaches and Migraines"]},
    "Celecoxib (Celebrex)": {"Ease of Use Score": 70, "Cost Score": 75, "Accessibility Score": 80, "Pain Treatment Score": 85, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Knee and Joint", "Arthritis"]},
    "Meloxicam (Mobic)": {"Ease of Use Score": 75, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 80, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Knee and Joint", "Headaches and Migraines"]},
    "Tramadol (Ultram)": {"Ease of Use Score": 70, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 90, "Adverse Effects Score": 80, "Duration Score": 85, "Affected Body Parts": ["Lower Back"]},
    "Cyclobenzaprine (Flexeril)": {"Ease of Use Score": 65, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 80, "Adverse Effects Score": 75, "Duration Score": 70, "Affected Body Parts": ["Neck and Shoulder", "Knee and Joint"]},
    "Methocarbamol (Robaxin)": {"Ease of Use Score": 65, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 80, "Adverse Effects Score": 70, "Duration Score": 70, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Knee and Joint"]},
    "Gabapentin (Neurontin)": {"Ease of Use Score": 75, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 75, "Adverse Effects Score": 75, "Duration Score": 85, "Affected Body Parts": ["Lower Back", "Hands and Wrists", "Knee and Joint" ]},
    "Pregabalin (Lyrica)": {"Ease of Use Score": 75, "Cost Score": 85, "Accessibility Score": 70, "Pain Treatment Score": 75, "Adverse Effects Score": 75, "Duration Score": 85, "Affected Body Parts": ["Nerves"]},
    "Oxycodone (Percocet)": {"Ease of Use Score": 70, "Cost Score": 75, "Accessibility Score": 65, "Pain Treatment Score": 90, "Adverse Effects Score": 80, "Duration Score": 75, "Affected Body Parts": ["Lower Back", "Knee and Joints", "Abdomen"]},
    "Amitriptyline (Elavil)": {"Ease of Use Score": 70, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 75, "Adverse Effects Score": 85, "Duration Score": 80, "Affected Body Parts": ["Nerves", "Headaches and Migraines", ""]},
    "Capsaicin cream": {"Ease of Use Score": 80, "Cost Score": 70, "Accessibility Score": 70, "Pain Treatment Score": 75, "Adverse Effects Score": 75, "Duration Score": 65, "Affected Body Parts": ["Knee and Joints", "Muslces", "Lower Back"]},
    "Lidocaine patches": {"Ease of Use Score": 75, "Cost Score": 70, "Accessibility Score": 80, "Pain Treatment Score": 75, "Adverse Effects Score": 70, "Duration Score": 70, "Affected Body Parts": ["Lower Back", "Joints", "Muscles"]},
    "Massage therapy": {"Ease of Use Score": 90, "Cost Score": 75, "Accessibility Score": 70, "Pain Treatment Score": 80, "Adverse Effects Score": 70, "Duration Score": 60, "Affected Body Parts": ["General Pain", "Lower Back", "Neck and Shoulders", "Legs", "Arms", "Feet"]},
    "Hyaluronic acid injections": {"Ease of Use Score": 60, "Cost Score": 50, "Accessibility Score": 50, "Pain Treatment Score": 70, "Adverse Effects Score": 60, "Duration Score": 70, "Affected Body Parts": ["Knee and Joint"]},
    "Corticosteroid injections": {"Ease of Use Score": 65, "Cost Score": 60, "Accessibility Score": 55, "Pain Treatment Score": 75, "Adverse Effects Score": 70, "Duration Score": 75, "Affected Body Parts": ["Joint", "Spine"]},
    "Glucosamine and chondroitin supplements": {"Ease of Use Score": 70, "Cost Score": 80, "Accessibility Score": 80, "Pain Treatment Score": 65, "Adverse Effects Score": 65, "Duration Score": 80, "Affected Body Parts": ["Knee and Joint"]},
    "Physical therapy exercises": {"Ease of Use Score": 85, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 80, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Knee and Joint"]},
    "Acupuncture": {"Ease of Use Score": 75, "Cost Score": 75, "Accessibility Score": 70, "Pain Treatment Score": 80, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Lower Back", "Neck and Shoulder", "Headaches and Migraines", "General Pain"]},
    "Knee braces/supports": {"Ease of Use Score": 80, "Cost Score": 70, "Accessibility Score": 85, "Pain Treatment Score": 70, "Adverse Effects Score": 65, "Duration Score": 85, "Affected Body Parts": ["Knee and Joint"]},
    "Excedrin": {"Ease of Use Score": 70, "Cost Score": 80, "Accessibility Score": 75, "Pain Treatment Score": 80, "Adverse Effects Score": 75, "Duration Score": 80, "Affected Body Parts": ["Headaches and Migraines"]},
    "Sumatriptan (Imitrex)": {"Ease of Use Score": 75, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 85, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Headaches and Migraines"]},
    "Rizatriptan (Maxalt)": {"Ease of Use Score": 75, "Cost Score": 80, "Accessibility Score": 70, "Pain Treatment Score": 85, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Headaches and Migraines"]},
    "Diclofenac potassium (Cambia)": {"Ease of Use Score": 75, "Cost Score": 85, "Accessibility Score": 70, "Pain Treatment Score": 85, "Adverse Effects Score": 70, "Duration Score": 85, "Affected Body Parts": ["Headaches and Migraines", "Muscles", "Joints"]},
    "Ergotamine derivatives": {"Ease of Use Score": 65, "Cost Score": 70, "Accessibility Score": 70, "Pain Treatment Score": 80, "Adverse Effects Score": 75, "Duration Score": 75, "Affected Body Parts": ["Headaches and Migraines"]},
    "Butalbital-containing medications": {"Ease of Use Score": 60, "Cost Score": 75, "Accessibility Score": 70, "Pain Treatment Score": 75, "Adverse Effects Score": 80, "Duration Score": 70, "Affected Body Parts": ["Headaches and Migraines"]},
    "Prochlorperazine (Compazine)": {"Ease of Use Score": 70, "Cost Score": 70, "Accessibility Score": 75, "Pain Treatment Score": 75, "Adverse Effects Score": 80, "Duration Score": 70, "Affected Body Parts": ["Headaches and Migraines"]},
    "Metoclopramide (Reglan)": {"Ease of Use Score": 70, "Cost Score": 75, "Accessibility Score": 75, "Pain Treatment Score": 75, "Adverse Effects Score": 80, "Duration Score": 70, "Affected Body Parts": ["Headaches and Migraines"]},
    "Dihydroergotamine (Migranal)": {"Ease of Use Score": 65, "Cost Score": 75, "Accessibility Score": 70, "Pain Treatment Score": 80, "Adverse Effects Score": 75, "Duration Score": 75, "Affected Body Parts": ["Headaches and Migraines"]},
    "Botulinum toxin injections (Botox)": {"Ease of Use Score": 60, "Cost Score": 70, "Accessibility Score": 65, "Pain Treatment Score": 80, "Adverse Effects Score": 75, "Duration Score": 70, "Affected Body Parts": ["Headaches and Migraines"]},
    "Amoxicillin": {"Ease of Use Score": 80, "Cost Score": 80, "Accessibility Score": 90, "Pain Treatment Score": 70, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Respiratory Tract", "Mouth"]},
    "Clindamycin": {"Ease of Use Score": 75, "Cost Score": 85, "Accessibility Score": 80, "Pain Treatment Score": 70, "Adverse Effects Score": 75, "Duration Score": 85, "Affected Body Parts": ["Mouth", "Bone", "Joint", "Respiratory Tract"]},
    "Lidocaine gel": {"Ease of Use Score": 80, "Cost Score": 75, "Accessibility Score": 85, "Pain Treatment Score": 75, "Adverse Effects Score": 70, "Duration Score": 75, "Affected Body Parts": ["Mouth", "Throat"]},
    "Benzocaine (Orajel)": {"Ease of Use Score": 85, "Cost Score": 70, "Accessibility Score": 85, "Pain Treatment Score": 70, "Adverse Effects Score": 75, "Duration Score": 70, "Affected Body Parts": ["Mouth"]},
    "Nonsteroidal anti-inflammatory gels like diclofenac (Voltaren) gel": {"Ease of Use Score": 80, "Cost Score": 75, "Accessibility Score": 85, "Pain Treatment Score": 75, "Adverse Effects Score": 70, "Duration Score": 75, "Affected Body Parts": ["Joint", "Muscle", "Back"]},
    "Antimicrobial mouth rinses": {"Ease of Use Score": 85, "Cost Score": 80, "Accessibility Score": 90, "Pain Treatment Score": 70, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Mouth", "Throat"]},
    "Chlorhexidine gluconate oral rinse": {"Ease of Use Score": 85, "Cost Score": 80, "Accessibility Score": 90, "Pain Treatment Score": 70, "Adverse Effects Score": 70, "Duration Score": 80, "Affected Body Parts": ["Mouth"]},
    "Dental anesthetics like articaine or lidocaine injections": {"Ease of Use Score": 75, "Cost Score": 75, "Accessibility Score": 85, "Pain Treatment Score": 75, "Adverse Effects Score": 70, "Duration Score": 75, "Affected Body Parts": ["Neck and Shoulder", "Knee and Joint"]}
}
# Define fuzzy variables
pain_treatment_effectiveness = ctrl.Antecedent(np.arange(0, 101, 1), 'pain_treatment_effectiveness')
adverse_effects = ctrl.Antecedent(np.arange(0, 101, 1), 'adverse_effects')
cost = ctrl.Antecedent(np.arange(0, 101, 1), 'cost')
body_part_relevance = ctrl.Antecedent(np.arange(0, 101, 1), 'body_part_relevance')
medication_desirability = ctrl.Consequent(np.arange(0, 101, 1), 'medication_desirability')

# Define fuzzy sets for body part relevance
body_part_relevance.automf(3)

# Define fuzzy sets for pain treatment effectiveness, adverse effects, and cost
pain_treatment_effectiveness.automf(3)
adverse_effects.automf(3)
cost.automf(3)

# Define fuzzy sets for medication desirability
medication_desirability['low'] = fuzz.trimf(medication_desirability.universe, [0, 0, 50])
medication_desirability['medium'] = fuzz.trimf(medication_desirability.universe, [25, 50, 75])
medication_desirability['high'] = fuzz.trimf(medication_desirability.universe, [50, 100, 100])

# Define fuzzy rules
rules = []
rules.append(ctrl.Rule(pain_treatment_effectiveness['poor'] | adverse_effects['poor'] | cost['poor'], medication_desirability['low']))
rules.append(ctrl.Rule(pain_treatment_effectiveness['average'] | adverse_effects['average'] | cost['average'], medication_desirability['medium']))
rules.append(ctrl.Rule(pain_treatment_effectiveness['good'] | adverse_effects['good'] | cost['good'], medication_desirability['high']))

# Create control system
medication_selection_ctrl = ctrl.ControlSystem(rules)
medication_selection = ctrl.ControlSystemSimulation(medication_selection_ctrl)

# Set inputs for the control system
medication_selection.input['pain_treatment_effectiveness'] = 0  # Initialize with a value, it will be overwritten later
medication_selection.input['adverse_effects'] = 0  # Initialize with a value, it will be overwritten later
medication_selection.input['cost'] = 0  # Initialize with a value, it will be overwritten later

# Select random medications
random_medications = random.sample(medication_data.keys(), 3)

# Define patient profiles
patient_profiles = []
for _ in range(1):
    locations = ["Lower Back", "Neck and Shoulder", "Knee and Joint", "Headaches and Migraines", "Dental"]
    pain_severity = random.randint(1, 10)
    location = random.choice(locations)
    patient_profiles.append({"Location": location, "Pain Severity": pain_severity})

# Lists to store desirability scores for each medication
desirability_scores = []

# Compute output for each patient profile and each medication
for profile in patient_profiles:
    print(f"\nPatient Profile: {profile}")
    print("Comparison of Selected Medications with Fuzzy Logic:")
    for medication in random_medications:
        affected_body_parts = medication_data.get(medication, {}).get("Affected Body Parts")
        if affected_body_parts and profile["Location"] not in affected_body_parts:
            print(f"\nMedication: {medication}")
            print(f"This medication is not suitable for treating {profile['Location']}.")
        else:
            medication_selection.input['pain_treatment_effectiveness'] = medication_data[medication]["Pain Treatment Score"]
            medication_selection.input['adverse_effects'] = medication_data[medication]["Adverse Effects Score"]
            medication_selection.input['cost'] = medication_data[medication]["Cost Score"]

            # Compute output
            medication_selection.compute()

            # Determine medication desirability
            desirability_score = medication_selection.output['medication_desirability'] / 100  # Normalize to 0-1 range

            print(f"\nMedication: {medication}")
            print("Pain Treatment Score:", medication_data[medication]["Pain Treatment Score"])
            print("Adverse Effects Score:", medication_data[medication]["Adverse Effects Score"])
            print("Cost Score:", medication_data[medication]["Cost Score"])
            print("Desirability Score (Normalized):", desirability_score)

            desirability_scores.append((medication, desirability_score))

            # Print why certain medication is the best
            if desirability_score >= 0.5:
                print("This medication is recommended due to its high desirability.")
            else:
                print("This medication is not recommended due to its low desirability.")

# Sort medications by desirability scores
sorted_medications = sorted(desirability_scores, key=lambda x: x[1], reverse=True)


# Print the prompt displaying top 3 medications, an okay medicine, and the worst medicine
print("\nTop Medications Based on Pain and Location:")
for i in range(len(sorted_medications)):
    print(f"{i+1}. {sorted_medications[i][0]}")


