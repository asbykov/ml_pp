import pandas as pd
import poly

def test_simple():
    assert 2 + 2 == 4

def test_main():

    df_test_input = pd.read_csv('tests/test_input.csv')

    assert len(df_test_input) == 50

    #df_pca, pca, scaler = poly.dim_reduction(df_test_input, 2)
    #assert len(df_pca) == 50

    df_test_output = pd.read_csv('tests/test_output.csv')
    assert len(df_test_output) == len(df_test_input)