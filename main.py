import blockchain
import plotting

voteBox = blockchain.Blockchain(difficulty=5)
voter = 0
candidates = {'A':0,'N':0,'R':0,'S':0}

print("---Welcome to Voting System---\n")

run = int(input("number of voters: "))

while voter < run:
    userVote = input("Vote for a candidate (A, N, R, S): ").upper()

    if userVote in candidates.keys():
        voteBox.addblock(userVote)
        candidates[userVote] += 1
        voter += 1
    else:
        print('invalid input')

print("\n--- Voting Results ---")
for candidate, votes in candidates.items():
    print(f'Candidate {candidate}: {votes} votes')

candidatesName = candidates.keys()
candidatesVotes = candidates.values()

plotting.plotWinners(candidatesName, candidatesVotes)

'''
print("\n--- Blockchain Details ---")
for block in voteBox.chain:
    print(f'Index: {block.index}, Vote: {block.vote}, Hash: {block.hashval}, Nonce: {block.nonce}, Previous Hash: {block.previous_hash}, Timestamp: {block.timestamp}')
'''

print("\n\n\n")
voteBox.validateBlockchain()



