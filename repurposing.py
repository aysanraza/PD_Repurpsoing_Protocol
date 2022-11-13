# Imports and Declaration


# function designed to find ns_fda_drugs from the "strong binders" prediction class results.
def approved_ns_predicted():
    # creating a list of ns_fda_drugs
    ns_fda_drugs = open("data/ns_fda_drugs.txt", "r")
    ns_fda_drugs_1 = ns_fda_drugs.readlines()
    for drug in range(len(ns_fda_drugs_1)):
        ns_fda_drugs_1[drug] = ns_fda_drugs_1[drug].lower()
    ns_fda_drugs_list = []
    for x in ns_fda_drugs_1:
        ns_fda_drugs_list.append(x.replace("\n", ""))
    list(ns_fda_drugs_list)
# creating a list of "strong" predicted drugs
    strong_predicted_drugs_list = []
    names = open("data/screen-drugs_ids_2.txt", "r")
    pred_strong = names.readlines()
    for ii in range(len(pred_strong)):
            pred_strong[ii] = pred_strong[ii].lower()
    for x in pred_strong:
        strong_predicted_drugs_list.append(x.replace("\n", ""))
    list(strong_predicted_drugs_list)
# comparing ns_fda_drugs with "strong" predicted results to find commons
    fda = list(set(strong_predicted_drugs_list) & set(ns_fda_drugs_list))
    print("Total of", len(fda), "drugs repurposed, given below: \n")
    print(fda)


if __name__ == '__main__':
    print("repurposing")
