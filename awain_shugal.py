# Imports and Declaration
import pandas as pd
from joblib import dump, load
global df3
import numpy as np


# function designed to extract feature that are not present in training dataset.
def main_list(df1,df2):
    col_1 = list(df1.columns)
    col_2 = list(df2.columns)
    main_list = list(set(col_1) - set(col_2))

    print(len(main_list))
    print ('Function 1 Completed')
    return main_list


def dropping(df1,main_list):
    df3 = df1.drop(main_list, axis=1) #dimention 1375
    df3 = df3.drop(['Lipinski','GhoseFilter','name'], axis=1) #dimentionality 1372
    df3 = df3.fillna(df3.mean()) #replace missinng value in coloum with the coloum mean
    df3 = df3.fillna(0)
    print(df3.shape)
    print('Function 2 Completed')
    return df3


def predict(df3):
    df = df3
    clf = load('ahsan1996x.joblib')
    result = (clf.predict(df))
    print('Function 3 Completed')
    return result

def strong_predict(df4):
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        strong_predictions = list(np.where(df4 == "Strong"))
        print(strong_predictions)
        df5 = pd.read_csv("drugsss_copy.csv", index_col=False)
        df6 = df5.Name

        with open(r"screen-drugs_ids_1.txt", "w") as fp:
            for i in strong_predictions:
                fp.write("%s\n" %df6[i]) #"%s\n"
        fp.close()

def approved_ns_predicted():
 # 1
    print ('start of function: final')
    f = open("ns_approved_drugs.txt", "r")
    ohh = f.readlines()
    for ib in range(len(ohh)):
        ohh[ib] = ohh[ib].lower()
    rep = []
    for x in ohh:
        rep.append(x.replace("\n", ""))
    list(rep)
    print(rep)
# 2
    rep1 = []
    f2 = open("screen-drugs_ids_2.txt", "r")
    pred_strong = f2.readlines()
    for ii in range(len(pred_strong)):
            pred_strong[ii] = pred_strong[ii].lower()
    for x in pred_strong:
        rep1.append(x.replace("\n", ""))
    list(rep1)
    print(rep1)
# 3
    common = list(set(rep1) & set(rep))
    print(len(common))
    print (common)


if __name__ == '__main__':
    # Data importation
    df1 = pd.read_csv("output2.csv")
    df2 = pd.read_csv("main2.csv")

    # Function callings
    main_list = main_list(df1, df2)  # f1
    df3 = dropping(df1, main_list)  # f1
    df4 = predict(df3)  # f3
    strong_predict(df4)  # f4
    approved_ns_predicted()  # f5


    print("\nProgram is ended ------------------------------------------------------------")
    #df4.to_csv("/home/ahsan/Desktop/final_results.txt", index=True)

