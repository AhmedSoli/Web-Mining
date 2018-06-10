from surprise import NMF
from surprise import Dataset
from surprise.model_selection import cross_validate

data = Dataset.load_builtin('ml-100k')
nmf = NMF()
cross_validate(nmf,data,measures=['RMSE'],cv=1,verbose=True)