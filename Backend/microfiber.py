from parse import category_type_dict

# dictionary to get fibre loss for each type
textileFibreLoss = {
  'polyester' : 161,
  'nylon' : 27,
  'natural' : 165
} 

def calculate_fibre_loss(lintTrap, softener, frontLoad, coldWater, textileType) :
  lintTrapModifier = 0.78 if lintTrap else 1;
  softenerModifier = 0.65 if softener else 1;
  frontLoadModifier = 1 if frontLoad else 7;
  coldWaterModifier = 0.7 if coldWater else 1;

  return textileFibreLoss[category_type_dict[textileType]] * lintTrapModifier * softenerModifier * frontLoadModifier * coldWaterModifier;


print(calculate_fibre_loss(True, True, True, True, 'organza'))
