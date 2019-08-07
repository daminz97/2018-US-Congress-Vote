import csv
import math


def load_csv():
	with open('congress_train.csv', newline='') as train_file:
		train_set = form_dataset(train_file)

	with open('congress_test.csv', newline='') as test_file:
		test_set = form_dataset(test_file)

	return train_set, test_set

def form_dataset(file):
	list = []
	reader = csv.reader(file, delimiter=' ', quotechar='|')
	for row in reader:
		list.append(str(' '.join(row)).split(','))
	return list

def countYea(t_set, index, target):
	count = 0
	for elem in t_set:
		if (elem[index] == 'Yea') and (elem[len(elem)-1] == target):
			count += 1
	return count

def countNay(t_set, index, target):
	count = 0
	for elem in t_set:
		if (elem[index] == 'Nay') and (elem[len(elem)-1] == target):
			count += 1
	return count

def countParty(t_set, target):
	count = 0;
	for elem in t_set:
		if elem[len(elem)-1] == target:
			count += 1
	return count

def countVotes(t_set, index):
	count = 0
	for elem in t_set:
		if elem[index] == 'Yea':
			count += 1
	return count

def predict(rep, dem, t_set):
	for elem in t_set:
		rep_score = 0
		dem_score = 0
		for i in range(len(elem)):
			rep_score += rep[i]
			dem_score += dem[i]

			if rep[i] >= dem[index]:
				print('Republican,' + str(rep[index]))
			else:
				print('Democrat,' + str(dem[index]))

def summary(l):
	count = 0
	for i in range(len(l)):
		count += l[i]
	return count


trainset, testset = load_csv()

# probability of party
rep_prob = countParty(trainset, 'Republican')
dem_prob = countParty(trainset, 'Democrat')
print(rep_prob, dem_prob)

rep_yea_count = []
rep_nay_count = []
dem_yea_count = []
dem_nay_count = []
vote_size = len(trainset[0])-1
# probability of votes and party
for i in range(vote_size):
	rep_yea_count.append(countYea(trainset, i, 'Republican'))
	rep_nay_count.append(countNay(trainset, i, 'Republican'))
	dem_yea_count.append(countYea(trainset, i, 'Democrat'))
	dem_nay_count.append(countNay(trainset, i, 'Democrat'))
print(summary(rep_yea_count), summary(dem_yea_count), summary(rep_nay_count), summary(dem_nay_count))



votes_given_rep = summary(rep_yea_count)/(summary(rep_yea_count)+summary(rep_nay_count))
votes_given_dem = summary(dem_yea_count)/(summary(dem_yea_count)+summary(dem_nay_count))
# probability of votes given party
# for j in range(vote_size):
# 	votes_given_rep.append(rep_yea_count[j]/rep_prob)
# 	votes_given_dem.append(dem_yea_count[j]/dem_prob)
print(votes_given_rep, votes_given_dem)


rep_given_votes = []
dem_given_votes = []
# probability of party given votes
for n in range(vote_size):
	rep_given_votes.append((votes_given_rep[n]*rep_prob))
	dem_given_votes.append((votes_given_dem[n]*dem_prob))
print(rep_given_votes_prob, dem_given_votes_prob)


rep_given_votes_prob = 0
dem_given_votes_prob = 0
for m in range(vote_size):
	rep_given_votes_prob += rep_given_votes[m]
	dem_given_votes_prob += dem_given_votes[m]


votes_prob = rep_given_votes_prob + dem_given_votes_prob

# new probability of party given votes
for a in range(vote_size):
	rep_given_votes[a] = rep_given_votes[a]/votes_prob
	dem_given_votes[a] = dem_given_votes[a]/votes_prob
























