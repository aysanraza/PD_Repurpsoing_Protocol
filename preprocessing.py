# Imports and Declaration

# function designed to extract features from input data that are not present in training dataset.
def preprocess_guide(df_molecular_descriptors, df_model_data):
    df_molecular_descriptors = list(df_molecular_descriptors.columns)
    df_model_data = list(df_model_data.columns)
    preprocess_guide = list(set(df_molecular_descriptors) - set(df_model_data))
    return preprocess_guide


# function designed to remove features from input data that are not present in training dataset.
def dropping(df_molecular_descriptors, preprocess_guide):
    preprocess_data = df_molecular_descriptors.drop(preprocess_guide, axis=1)  # dimension 1375
    preprocess_data = preprocess_data.drop(['Lipinski', 'GhoseFilter', 'name'], axis=1)  # dimension 1372
    preprocess_data = preprocess_data.fillna(preprocess_data.mean())  # replace missing value with the column mean
    preprocess_data = preprocess_data.fillna(0)
    return preprocess_data


if __name__ == '__main__':

    print("preprocessing")
