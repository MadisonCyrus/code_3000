import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    identifiers = ["age", "zip3", "gender"]
    merged = anon_df.merge(aux_df, on=identifiers) 
    merged = merged.drop_duplicates(subset="anon_id", keep=False)
    merged = merged.rename(columns={"name": "matched_name"})
    return merged[["anon_id", "matched_name"]]
    #raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    x = matches_df.shape
    y = anon_df.shape
    return x[0]/y[0]
    #raise NotImplementedError
