import pandas as pd
import numpy as np

from poly import dim_reduction

def test_main():

    # very simple integration test

    df_test_input = pd.read_csv('tests/test_input.csv')

    assert len(df_test_input) == 50

    features = ['eu_position', 'eu_position_sd',
                'eu_salience',  'lrgen', 'lrecon', 'lrecon_sd',
                'lrecon_salience', 'lrecon_dissent', 'galtan',
                'galtan_sd', 'galtan_salience', 'galtan_dissent',
                'immigrate_policy', 'immigrate_salience',
                'multiculturalism',
                'redist_salience', 'environment', 'enviro_salience',
                'deregulation', 'econ_interven',
                'sociallifestyle', 'religious_principles',
                'urban_rural',
                'russian_interference', 'people_vs_elite',
                'antielite_salience', 'corrupt_salience']

    index_features = ['country', 'party', 'party_id']

    df_pca, pca, scaler = dim_reduction(df_test_input, 2, features, index_features)

    assert len(df_pca) == 50

    df_test_output = pd.read_csv('tests/test_output.csv')
    assert len(df_test_output) == len(df_pca)


    for col in df_pca.columns:
        if col[0:2] == 'pc':
            assert len(df_test_output[col].apply(np.round) == df_pca[col].apply(np.round)) == 50

