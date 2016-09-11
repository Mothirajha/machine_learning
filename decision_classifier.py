# Weight |  Texture  | Label
#  150g  |   Bumpy   | Orange
#  170g  |   Bumpy   | Orange
#  140g  |  Smooth   | Apple
#  150g  |  Smooth   | Apple
#  ....  |   .....   | ......

# More the training data - More the accuracy

# This is the simplest classifier to visulize where the decision is been taken by the machine.

from sklearn import tree

# features = [[150, "Bumpy"], [170, "Bumpy"], [140, "Smooth"], [150, "Smooth"]]
# labels = ["orange", "organe", "apple", "apple"]

features = [[150, 0], [170, 0], [140, 1], [150, 1]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print clf.predict([[170, 1]])

