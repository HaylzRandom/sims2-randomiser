import inquirer
from sim_personality.generator import generate_sim

print("Sims 2 Sim Tool")

choice = inquirer.list_input(
    "What would you like to do?",
    choices=["1. Generate a Sim", "2. Generate Traits for Sim"],
)

if choice == "1. Generate a Sim":
    generate_sim()
else:
    # Generate Traits/Aspiration for Sim
    print("Other!")

