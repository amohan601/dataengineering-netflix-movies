import io
import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import os

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    input_url = os.environ.get('INPUT_URL')
    #print(variable_value)
    #url = kwargs['INPUT_URL']
    return pd.read_csv(input_url, sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
