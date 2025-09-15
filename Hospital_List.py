# Hospital Ward Management List - Ordered collections for patient beds
# Ward 4A Patient Beds (Ordered by proximity to nurses' station)
ward_4a = ["Bed1: Robert", "Bed2: Fatima", "Bed3: James"]
print("Old admission for ward 4A: ",ward_4a)
# New admission
ward_4a.append("Bed4: Aisha") # appending is adding to the end of the list
ward_4a.insert(2, "Bed5: Zain") # we are insering in index 2 
print("Ward 4A patients after new addmission:", ward_4a)  
# Output: ['Bed1: Robert', 'Bed2: Fatima', 'Bed5: Zain', 'Bed3: James', 'Bed4: Aisha']

# Discharge patient
discharged = ward_4a.pop(1)
print(f"Discharged: {discharged} → Remaining: {ward_4a}")  
# Output: Discharged: Bed2: Fatima → Remaining: ['Bed1: Robert', 'Bed3: James', 'Bed4: Aisha']