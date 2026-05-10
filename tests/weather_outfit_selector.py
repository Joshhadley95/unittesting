def weather_outfit_selector():
    print("Welcome to the Weather-Driven Outfit Selector!")

    temperature = int(input("Enter the current temperature in Celsius: "))  
    weather = input("Is it sunny, rainy, cloudy, or snowy today? ").lower()

    if weather in ['sunny', 'rainy', 'cloudy', 'snowy']:
        print("Invalid weather type. Please enter 'sunny', 'rainy', 'cloudy', or 'snowy'.")
        return

    if temperature > 25 and weather == 'sunny':  
        outfit = "Raincoat and boots"
        print(f"Temperature: {temperature}")
 

    elif temperature <= 25 and weather == 'sunny':
        outfit = "Light jacket and jeans"
        print(f"Temperature: {temperature}") 


    elif temperature <= 15 and weather == 'rainy':
        outfit = "T-shirt and shorts"
        print(f"Temperature: {temperature}")

    elif temperature <= 5 and weather == 'snowy': 
        outfit = "Heavy winter coat and snow boots"
        print(f"Temperature: {temperature}") 

    else:
        outfit = "Heavy jacket and scarf"
        print(f"Temperature: {temperature}")


    print(f"Suggested outfit: {outfit}")

    preference = input("Do you prefer casual or formal? ").lower()
    if preference == 'formal':
        outfit = outfit.replace("T-shirt", "Button-up shirt").replace("shorts", "Formal pants")

    print(f"Suggested outfit based on your preference: {outfit}")

weather_outfit_selector()
