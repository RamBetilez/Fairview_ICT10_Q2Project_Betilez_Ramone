from pyscript import document,display

non_metals = {"H": ('Hydrogen', 1, 1.008),
              "He": ('Helium', 2, 4.0026),
              "C": ('Carbon', 6, 12.011),
              "N": ('Nitrogen', 7, 14.007),
              "O": ('Oxygen', 8, 15.999),
              "F": ('Fluorine', 9, 18.998),
              "Ne": ('Neon', 10, 20.180),
              "P": ('Phosphorus', 15, 30.974),
              "S": ('Sulfur', 16, 32.06),
              "Cl": ('Chlorine', 17, 35.45),
              "Ar": ('Argon', 18, 39.948),
              "Se": ('Selenium', 34, 78.971),
              "Br": ('Bromine', 35, 79.904),
              "Kr": ('Krypton', 36, 83.798),
              "I": ('Iodine', 53, 126.90),
              "Xe": ('Xenon', 54, 131.29),
              "At": ('Astatine', 85, 210),
              "Rn": ('Radon', 86, 222),
              "Ts": ('Tennessine', 117, 294),
              "Og": ('Oganesson', 118, 294)}

# function to search your planet
def Search_Element(e):
    # Get the Input from HTML

    elements_1 = document.getElementById("elementz").value
    # retrieve info from the dictionary

    result = non_metals.get(elements_1, ('Non-Metal Element not found', "-", "-"))
    # display the result in HTML
    document.getElementById("code").innerText = elements_1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]