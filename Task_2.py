
# Getting Started
def validate_Format(reading): # Function Validating the format of the speed readings or if it is empty
    assert reading != ""
    if (reading.capitalize()[0] not in ["E", "U"]) or any(char.isalpha() for char in reading[1:len(reading)+1]):
        raise ValueError
        
def conversion(reading): # Function for checking the type of the readings(E for European and U for British) and converting and returning the tuple
    if reading[0].upper() == "E":
        reading_in_km = float(reading[1:len(reading)+1])
        reading_in_miles = reading_in_km / 1.60934

    else :
        reading_in_miles  = float(reading[1:len(reading)+1])
        reading_in_km = reading_in_miles * 1.60934
        
    return (reading_in_miles, reading_in_km)


print("Swallow Speed Analysis: Version 1.0")
reading_list = [] # List for storing the readings
while True:
    try:
        reading = input("Enter the Next Reading : ")
        validate_Format(reading)

        # storing the tuple in list for easy use
        reading_tuple = conversion(reading)
        reading_list.append(reading_tuple)
    
    except ValueError as e:
        print("Invalid Input Format!!! Try Again")

    except AssertionError as e:
        break
        
               
if reading_list == []:
    print("No readings entered. Nothing to do.")
    
else :
    # Calculating the max, min and average readings
    max_reading = max(reading_list)
    min_reading = min(reading_list)
    
    avg_reading_in_miles = sum([x[0] for x in reading_list])/len(reading_list)
    avg_reading_in_km = sum([x[1] for x in reading_list])/len(reading_list)
    
    # Output Part
    print("\nResults Summary")
    print(f"{len(reading_list)} Readings analyzed.\n")
    
    print(f"Max Reading : {max_reading[0]:.1f} MPH, {max_reading[1]:.1f} KPH")
    print(f"Min Reading : {min_reading[0]:.1f} MPH, {min_reading[1]:.1f} KPH")
    print(f"Average Reading : {avg_reading_in_miles:.1f} MPH, {avg_reading_in_km:.1f} KPH")