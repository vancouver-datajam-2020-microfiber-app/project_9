import pandas as pd

import pandas as pd

# load csv file
category_type_df = pd.read_csv("../Data/category_type.csv", index_col=1, squeeze = True)
male_clothing_weight_df = pd.read_csv("../Data/clothing_weight_m.csv")
female_clothing_weight_df = pd.read_csv("../Data/clothing_weight_w.csv")

# convert to dict
category_type_dict = category_type_df.to_dict()
male_clothing_weight_dict = male_clothing_weight_df.to_dict('records')
female_clothing_weight_dict = female_clothing_weight_df.to_dict('records')
