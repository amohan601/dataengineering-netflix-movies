if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    data = data.convert_dtypes()
    data['Hours Viewed'] = pd.to_numeric(data['Hours Viewed'], errors= 'coerce')
    data['Number of Ratings'] = pd.to_numeric(data['Number of Ratings'], errors= 'coerce')
    data['Rating'] = pd.to_numeric(data['Rating'], errors= 'coerce')
    data['release_date_ts'] = pd.to_datetime(data['Release Date'],format='%Y-%m-%d', errors= 'coerce')
    print('hey')
    data['rs'] =  pd.to_datetime(data['Release Date'],format='%Y-%m-%d', errors= 'coerce').dt.date
    print('hey1')
    data['Genre'] = data['Genre'].str.lstrip('[')
    data['Genre'] = data['Genre'].str.rstrip(']')
    print(data.dtypes)

    data = data.rename(columns={
                        'Title':'title',
                        'Available Globally?':'availability',
                        'Release Date':'release_date',
                        'Hours Viewed':'hours_viewed',
                        'Number of Ratings':'number_of_ratings',
                        'Rating':'rating',
                        'Genre':'genre',
                        'Key Words':'keywords',
                        'Description':'description'})
    print('shape before clean up', data.shape)
    data = data.dropna(subset=['release_date_ts','number_of_ratings','rating'])
    print('shape after clean up', data.shape)
    #data['year_month'] = data['release_date_ts'].dt.to_period('M')
    data['month'] = data['release_date_ts'].dt.month
    data['year'] = data['release_date_ts'].dt.year
    data = data.drop(columns=['release_date_ts'], axis=1)
    print(data.dtypes)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
