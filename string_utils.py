def split_before_each_uppercases(formula):
    split_formula = []
    
    if not formula:
      return split_formula
    start = 0
    end = 1
    for i in formula [1:]:
      if i.isupper():
        split_part = formula[start:end]
        split_formula.append(split_part)
        start = end
      end +=1
    split_formula.append(formula[start:end])
    return split_formula

def split_at_first_digit(formula):
  digit_location = 1
  for i in formula [1:]:
    if not i.isdigit():
      digit_location += 1
    elif i.isdigit ():
      break
  if digit_location == len(formula):
    return (formula , 1)
  else:
    new_formula_1 = formula[:digit_location]
    new_formula_2 = formula[digit_location:]
    return (new_formula_1 , int(new_formula_2))

def count_atoms_in_molecule(formula):
  mol_dict = {}
  result = split_before_each_uppercases(formula)
  for i in result:
    result2 = split_at_first_digit(i)
    mol_dict[result2[0]] = int(result2[1])
  return mol_dict
  for atom in split_before_each_uppercases(molecular_formula):
      atom_name, atom_count = split_at_first_digit(atom)

    # Step 1: Initialize an empty dictionary to store atom counts
        
        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
