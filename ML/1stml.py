from sklearn import tree
#print(sklearn.__version__)
#print("hello dax")
features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,labels) #training the model with features and labels 
print(clf.predict([[150,1]]))