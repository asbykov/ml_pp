from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd


def dim_reduction(df, n_dim, features, index_features, scaler=None, pca=None):
    # Input:
    # Pandas DataFrame df - data of political parties
    # integer n_dim - Number of desired dimensions in the output dataset. Has to be >= 2
    # List features - list of strings of features that we want dimensionality reduction method to be applied to
    # List index_features - list of index features (like names, and id's)
    # Object scaler - sklearn Scaler object (if you want to use pre-defined scaler)
    # Object pca - sklearn PCA object (if you want to use an existing scaler)
    #
    # Output:
    # Pandas Dataframe df_pca  - dataset where features are replaced by n_dim principal components
    # Object scaler - sklearn Scaler object (same or newly created)
    # Object pca - sklearn PCA object (same or newly created)

    assert n_dim >= 2

    # Part 1: Normalisation
    # check if no scaler is provided, create a new one in that case
    if scaler is None:
        scaler = StandardScaler()
        scaler.fit(df[features])

    # Do actual transformation
    x = scaler.transform(df[features])

    # Part 2: PCA
    # Create new PCA (if none provided), use n_dim as a number of dimensions
    if pca is None:
        pca = PCA(n_components=n_dim)

    # Dimensionality reduction using PCA
    principalComponents = pca.fit_transform(x)

    # make names for new principal components
    pc_columns = []
    for i in range(n_dim):
        pc_columns.append('pc_' + str(i + 1))

    # Convert numpy array to Pandas Dataframe
    principalDf = pd.DataFrame(data=principalComponents, columns=pc_columns)

    # Concatenate index features back to the dataset
    df_pca = pd.concat([principalDf, df[index_features]], axis=1)

    return df_pca, pca, scaler
