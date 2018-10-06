from sklearn import svm, metrics
datas = [[0,0], [0,1], [1,0], [1,1]]
labels = [0, 1, 1, 0]
examples = [[0,0], [0,1]]
examples_label = [0,1]

clf = svm.SVC()
# clf.fit(데이터, 답)
clf.fit(datas, labels)
result = clf.predict(examples) # --> [0, 1]

print(result)

score = metrics.accuracy_score(examples_label, result)
print("정답률 : ", score)