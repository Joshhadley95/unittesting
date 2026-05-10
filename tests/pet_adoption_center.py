import unittest
import warnings

# Function to match a pet with an adopter based on preferences
def match_pet(adopter_preferences, pets):
    for pet in pets:
        if (
            (adopter_preferences["type"] and adopter_preferences["type"] == pet["type"]) or
            (adopter_preferences["size"] and adopter_preferences["size"] == pet["size"]) or
            (adopter_preferences["age"] and adopter_preferences["age"] == pet["age"])
        ):
            return pet["name"]
    return "No match found"

# Function to calculate adoption fee based on the pet's age
def calculate_adoption_fee(pet_age):
    if pet_age < 0:
        return "Invalid age" 
    elif pet_age < 2:
        return 100  # Younger pets have higher fees
    return 50  # Adult pets have lower fees

# Function to add a new pet to the adoption list
def register_new_pet(new_pet, adoption_list):
    if any(existing_pet["name"] == new_pet["name"] for existing_pet in adoption_list):
        warnings.warn(f"{new_pet['name']} is already in the adoption list", UserWarning)
    else:
        adoption_list.append(new_pet)
    return adoption_list

class TestPetAdoptionCenter(unittest.TestCase):
    
    def setUp(self):
        self.pets = []

    def tearDown(self):
        self.pets = None

    def test_match_pet(self):
        pets = [
            {"name": "Buddy", "type": "Dog", "size": "Medium", "age": 3},
            {"name": "Mittens", "type": "Cat", "size": "Small", "age": 1},
            {"name": "Charlie", "type": "Dog", "size": "Large", "age": 5}
        ]
        self.assertEqual(match_pet({"type": "Dog", "size": "", "age": ""}, pets), "Buddy")
        self.assertEqual(match_pet({"type": "", "size": "Small", "age": ""}, pets), "Mittens")
        self.assertEqual(match_pet({"type": "", "size": "", "age": 5}, pets), "Charlie")
        self.assertEqual(match_pet({"type": "", "size": "", "age": 10}, pets), "No match found")

    def test_calculate_adoption_fee(self):
        self.assertEqual(calculate_adoption_fee(1), 100)
        self.assertEqual(calculate_adoption_fee(3), 50)
        self.assertEqual(calculate_adoption_fee(-1), "Invalid age")

    def test_register_new_pet(self):
        pets = [
            {"name": "Buddy", "type": "Dog", "size": "Medium", "age": 3},
            {"name": "Mittens", "type": "Cat", "size": "Small", "age": 1}
        ]
        self.assertEqual(register_new_pet({"name": "Charlie", "type": "Dog", "size": "Large", "age": 5}, pets), pets)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            register_new_pet({"name": "Buddy", "type": "Dog", "size": "Medium", "age": 3}, pets)
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, UserWarning))
            self.assertIn("Buddy is already in the adoption list", str(w[-1].message))

    @unittest.skip("Adding more pet options")
    def test_add_more_pet_options(self):
        pets = [
            {"name": "Buddy", "type": "Parrot", "size": "5 inches", "age": "3.5 years"},
            {"name": "Mittens", "type": "Cat", "size": "Small", "age": 1}
        ]
        self.assertEqual(register_new_pet({"name": "Buddy", "type": "Parrot", "size": "5 inches", "age": "3.5 years"}, pets), pets)

if __name__ == "__main__":
    unittest.main()
