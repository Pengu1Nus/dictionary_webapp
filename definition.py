import pandas

df = pandas.read_csv('data.csv')


class Definition:
    def __init__(self, term: str):
        self.term = term.strip()

    def get(self):
        dataframe = pandas.read_csv('data.csv')
        return tuple(
            dataframe.loc[dataframe['word'] == self.term]['definition']
        )
