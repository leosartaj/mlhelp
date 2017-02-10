from sklearn.base import BaseEstimator, TransformerMixin


class MultiLabelEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None):
        self.cols = cols

    def fit(self, X, y=None):
        assert(type(self.cols) == list), 'cols should be a list of column names/indexes'
        self.encoders_ = {}
        for col in self.cols:
            if type(col) == int:
                loc = X.iloc[:, col]
            else:
                loc = X.loc[:, col]
            enc = LabelEncoder()
            enc.fit(loc)
            self.encoders_[col] = enc
        return self

    def transform(self, X):
        new_X = X.copy()
        for col in self.cols:
            if type(col) == int:
                new_X.iloc[:, col] = self.encoders_[col].transform(X.iloc[:, col])

            else:
                new_X.loc[:, col] = self.encoders_[col].transform(X.loc[:, col])
        return new_X

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)
