import math

# Example comma-separated string
audio_data_str = "0.1,0.2,0.3,0.4"

# Step 1: Parse the comma-separated string
audio_data = [float(value) for value in audio_data_str.split(',')]

# Step 2: Calculate decibel values
def calculate_decibel(value):
    reference_amplitude = 1.0  # Adjust this if your reference amplitude is different
    return 20 * math.log10(value / reference_amplitude)

# Apply the decibel calculation to each value in the audio data
decibel_values = [calculate_decibel(value) for value in audio_data]

# Print the resulting decibel values
print(decibel_values)