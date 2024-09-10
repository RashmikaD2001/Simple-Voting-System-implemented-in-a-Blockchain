import blockchain
import plotting

voteBox = blockchain.Blockchain(difficulty=4)
voter = 0
candidates = {}
#candidates = {'A':0,'N':0,'R':0,'S':0}

print("---Welcome to Voting System---\n")

print("Enter candidate to the voting system")
candidateNo = int(input("Enter candidate number: "))

for i in range(candidateNo):
    nameOfCandidate = input(f"Enter {i+1} candidate name: ").upper()
    candidates[nameOfCandidate] = 0

run = int(input("number of voters: "))

if run>0 and len(candidates)>0:
    while voter < run:
        userVote = input(f"Vote for a candidate ({','.join(list(candidates.keys()))}): ").upper()

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



