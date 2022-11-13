# Imports and Declaration
import pandas as pd
import preprocessing
import virtual_screening
import repurposing

if __name__ == '__main__':
    # Data importation
    df_molecular_descriptors = pd.read_csv("data/molecular_descriptors.csv")
    df_model_data = pd.read_csv("data/model_data.csv")

    # Function callings
    # preprocessing of the input data
    preprocess_guide = preprocessing.preprocess_guide(df_molecular_descriptors, df_model_data)
    preprocess_data = preprocessing.dropping(df_molecular_descriptors, preprocess_guide)
    # predictions of strong inhibitor
    prediction_data = virtual_screening.predict(preprocess_data)
    strong_predict = virtual_screening.strong_predict(prediction_data)
    # repurposing ns_fda_drugs
    repurposing.approved_ns_predicted()



