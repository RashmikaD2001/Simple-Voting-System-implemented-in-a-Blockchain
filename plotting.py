import matplotlib.pyplot as plt

def plotWinners(candidatesName, candidatesVotes):
    fig = plt.figure(figsize=(10, 5))

    plt.bar(candidatesName, candidatesVotes, color='black', width=0.4)

    plt.xlabel("Candidates' name")
    plt.ylabel("No. of Votes")
    plt.title("Number of votes by each candidates")
    plt.show()

if __name__ == '__main__':
    print("this is the implementation of plotting the votes")