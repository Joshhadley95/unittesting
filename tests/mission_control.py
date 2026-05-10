import unittest
import warnings

# Function to calculate gravity based on the planet
def calculate_gravity(planet):
    planet_gravity = {
        "Earth": 9.8,
        "Mars": 3.7,
        "Venus": 8.87
    }
    if planet not in planet_gravity:
        return "Unknown planet"
    return planet_gravity[planet]


def check_astronaut_health(health_score):
    if health_score < 0:
        return "Invalid health score"
    elif health_score < 50:
        return "Astronaut not fit for the mission"
    return "Astronaut is fit for the mission"


def add_planet_to_mission(planet, mission_plan):
    if planet in mission_plan:
        warnings.warn(f"{planet} is already in the mission plan", UserWarning)
    else:
        mission_plan.append(planet)
    return mission_plan

# Test case class for Astronauts' Space Mission
class TestMissionControl(unittest.TestCase):
    
    def setUp(self):
        self.mission_plan = []
    

    def test_calculate_gravity(self):
        result = calculate_gravity("Earth")
        self.assertEqual(result, 9.8)

        result = calculate_gravity("Pluto")
        self.assertEqual(result, "Unknown planet")

    def test_check_astronaut_health(self):
        result = check_astronaut_health(80)
        self.assertEqual(result, "Astronaut is fit for the mission")

        result = check_astronaut_health(30)
        self.assertEqual(result, "Astronaut not fit for the mission")

        result = check_astronaut_health(-10)
        self.assertEqual(result, "Invalid health score")

    def test_add_planet_to_mission(self):
        mission_plan = add_planet_to_mission("Mars", self.mission_plan)
        self.assertIn("Mars", mission_plan)

        with self.assertWarns(UserWarning):
            mission_plan = add_planet_to_mission("Mars", self.mission_plan)
        self.assertEqual(mission_plan.count("Mars"), 1)  # Ensure Mars is not added twice


    @unittest.skip("Skipping this test for now.")
    def test_add_sun_to_mission(self):
        mission_plan = add_planet_to_mission("Sun", self.mission_plan)
        self.assertIn("Sun", mission_plan)

    


if __name__ == "__main__":
    unittest.main()
