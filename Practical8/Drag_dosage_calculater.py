def calculate_paracetamol_volume(weight, strength):
    # Check weight validity
    if not (10 <= weight <= 100):
        return("Error: Weight must be between 10 and 100 kg")
    # Check strength validity
    if strength not in [120, 250]:
        return("Error: Strength must be either 120 mg/5ml or 250 mg/5ml")
    # Calculate required volume in ml
    dose_mg = 15 * weight
    volume_ml = (dose_mg / strength) * 5
    return volume_ml
    
weight = int(input("enter the weight in kilograms: "))
strength = int(input("enter the strength: "))
result = calculate_paracetamol_volume(weight, strength)
print(f"the volume of paracetamol required: {result} ")
# Example function call
print(calculate_paracetamol_volume(20, 120))  # Output: 12.5