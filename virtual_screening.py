# Imports and Declaration
import pandas as pd
from joblib import dump, load
import numpy as np


# function designed to perform predictions on input dataset
def predict(preprocess_data):
    input_data = preprocess_data
    clf = load('model.joblib')
    result = (clf.predict(input_data))
    return result


# function designed to extract only the "strong binders" prediction class results
def strong_predict(prediction_data):
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        strong_predictions = list(np.where(prediction_data == "Strong"))
        drug_names = pd.read_csv("data/atc_level_1.csv", index_col=False)
        drug_names_list = drug_names.Name

        with open(r"data/strong_predict_ids.txt", "w") as fp:
            for i in strong_predictions:
                fp.write("%s\n" % drug_names_list[i])
        fp.close()


if __name__ == '__main__':
    print("virtual_screening")
