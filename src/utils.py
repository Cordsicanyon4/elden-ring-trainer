import os

# Function to boost character stats
def boost_stat(boost_value):
    print(f"Boosting character stats by {boost_value}.")

# Function to modify item properties
def modify_item():
    print("Modifying item properties.")

# Function for quick save and load
def quick_save_load():
    print("Quick save and load enabled.")

# Function to run custom scripts
# Example: run a script that changes game settings
# Note: This should be adapted for your specific use case
# def run_custom_script(path):
#     if os.path.exists(path):
#         print(f"Running custom script from {path}.")
#         exec(open(path).read())
#     else:
#         print(f"Script path {path} does not exist.")