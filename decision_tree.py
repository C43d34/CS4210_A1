#-------------------------------------------------------------------------
# AUTHOR: Cleighton Greer
# FILENAME: decision_tree.py
# SPECIFICATION: build decision tree from .csv input file
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
        #  print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]

##Get column (unique) values across all rows (assume all inputs are string)
list_of_column_key_val_mappings = []

  #iterate through every column to get the values
for col in range(0, len(db[0])-1): #skip last column which is the class label
  unique_column_vals = []
  for row in range(0, len(db)):
    unique_column_vals.append(db[row][col])

  unique_column_vals = set(unique_column_vals)
  list_of_column_key_val_mappings.append(dict([[pair[1], pair[0]] for pair in enumerate(unique_column_vals)]))


##Transform data (feature values) using generated column key/value mapping
  #iterate through every row minus
for row in range(0, len(db)):
  new_row_of_X = []
  for col in range(0, len(db[0])-1): #skip last column which is the class label
    new_row_of_X.append(list_of_column_key_val_mappings[col][db[row][col]]) # mappings: [which column][key] = corresponding integer value
  X.append(new_row_of_X)

print(X)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

##Do same as above but exclusively for the last column of the data
unique_column_vals = []
for row in range(0, len(db)):
  unique_column_vals.append(db[row][-1])

unique_column_vals = set(unique_column_vals)
list_of_column_key_val_mappings.append(dict([[pair[1], pair[0]] for pair in enumerate(unique_column_vals)]))

##Transform class label values using generated column key/value mapping
for row in range(0, len(db)):
  Y.append(list_of_column_key_val_mappings[-1][db[row][-1]])

print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

# #plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()