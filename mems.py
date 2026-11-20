from pyscript import document, display

# Predefine grade level sets with initial members[cite: 3]
grade7 = {'Ram Betilez', 'Ram Amortizado', 'Ram Magtanggol', 'Ram Correa', 'Ram Evangelista'}
grade8 = {'Ram Maniago', 'Ram Caagbay', 'Ram Alip', 'Ram Agacita', 'Ram Lao'}
grade9 = {'Ram Buntile', 'Ram Ramos', 'Ram Concengco', 'Ram Chua', 'Ram Coronel', 'Ram Pagud', 'Ram Pagsanhan'}
grade10 = {'Ram Montefalco', 'Ram Mondragon', 'Ram Canedo', 'Ram Catu'}

# Combine all grade sets into a master set using set union[cite: 3]
master_set = grade7 | grade8 | grade9 | grade10

def verify(e):
# Retrieve and format user input values[cite: 3]
first_name = document.getElementById("firstname").value.strip()
last_name = document.getElementById("lastname").value.strip()
full_name = f"{first_name.title()} {last_name.title()}"

# Add new member to master set using set union operator[cite: 3]
all_members = master_set | {full_name}