# Simple Linear Regression for GreenRoute
# Predicts fuel (L/100km) based on cargo weight (kg)

def predict_fuel(weight):
    # Base consumption + (coefficient * weight)
    # y = a + bx
    base_consumption = 8.5 
    weight_coefficient = 0.002 
    
    prediction = base_consumption + (weight_coefficient * weight)
    return prediction

# Test with a 500kg load
cargo = 500
print(f"Predicted fuel consumption for {cargo}kg load: {predict_fuel(cargo)} L/100km")
