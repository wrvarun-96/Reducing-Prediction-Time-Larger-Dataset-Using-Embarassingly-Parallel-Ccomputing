import time
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.ensemble import RandomForestClassifier



df = pd.read_csv('/Users/varun/Documents/data.csv')

outliers=[]
def detect_outlier(data):
    
    threshold=3
    mean = np.mean(data)
    std =np.std(data)
    
    
    for y in data:
        z_score= (y - mean)/std
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers


for i in df.columns:
    data_new = df[i].astype(float)
    outlier_datapoints = detect_outlier(data_new)
    #print(outlier_datapoints)
    
#No outliers are present in this dataframe

#Checking for multicollinearity
sns.pairplot(df)



# define feature selection
fs = SelectKBest(score_func=f_regression, k=4)
# apply feature selection

X=df.drop(['book_genre'],axis=1)
y=df['book_genre']

X_selected = fs.fit_transform(X, y)
#print(X_selected.shape)

#Final selected featurs are 
#author_id
#book_rating
#publish_year
#text_lang


genre_features = ['author_id', 'book_rating', 'publish_year', 'text_lang']
genre_target = 'book_genre'


X = df[genre_features]
Y = df[genre_target]


# define standard scaler
scaler = StandardScaler()
X_scaled=scaler.fit_transform(X)



s1=time.time()
clf=RandomForestClassifier(n_estimators=100,random_state=0,n_jobs=8)
new_model=clf.fit(X.values,Y.values)
e1=time.time()

print('Time taken to train using 8 cores is ', e1-s1)
