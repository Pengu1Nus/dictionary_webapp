import pandas

df = pandas.read_csv('data.csv')


class Definition:
    def __init__(self, term: str):
        self.term = term.strip()

    def get(self):
        dataframe = pandas.read_csv('data.csv')
        matched_rows = dataframe.loc[
            dataframe['word'].str.contains(self.term, case=False, na=False)
        ]
        return tuple(matched_rows['definition'])
