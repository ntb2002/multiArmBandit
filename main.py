import random


def c1happy():
    happy = random.normalvariate(10, 8)
    return happy


def c2happy():
    happy = random.normalvariate(15, 6)
    return happy


def c3happy():
    happy = random.normalvariate(12, 5)
    return happy


def exploitOnly():
    happinessList = []
    happinessList.append(c1happy())
    happinessList.append(c2happy())
    happinessList.append(c3happy())

    highNum = happinessList[0]
    for i in happinessList:
        if i > highNum:
            highNum = i

    if highNum == happinessList[0]:
        for i in range(297):
            happinessList.append(c1happy())

    elif highNum == happinessList[1]:
        for i in range(297):
            happinessList.append(c2happy())

    else:
        for i in range(297):
            happinessList.append(c3happy())

    return sum(happinessList)


def exploreOnly():
    happinessList = []

    for i in range(100):
        happinessList.append(c1happy())

    for i in range(100):
        happinessList.append(c2happy())

    for i in range(100):
        happinessList.append(c3happy())

    return sum(happinessList)


def eGreedy(e):
    happinessList = []
    c1 = []
    c2 = []
    c3 = []

    happinessList.append(c1happy())
    c1.append(c1happy())
    happinessList.append(c2happy())
    c2.append(c2happy())
    happinessList.append(c3happy())
    c3.append(c3happy())

    for i in range(300):
        r = random.random() * 100
        if r < e:
            cafe = random.randint(1, 3)

            if cafe == 1:
                happinessList.append(c1happy())
                c1.append(c1happy())

            elif cafe == 2:
                happinessList.append(c2happy())
                c2.append(c2happy())

            else:
                happinessList.append(c3happy())
                c3.append(c3happy())

        else:
            c1avg = sum(c1) / len(c1)
            c2avg = sum(c2) / len(c2)
            c3avg = sum(c3) / len(c3)

            if c1avg > c2avg and c1avg > c3avg:
                happinessList.append(c1happy())
                c1.append(c1happy())

            elif c2avg > c1avg and c2avg > c3avg:
                happinessList.append(c2happy())
                c2.append(c2happy())

            else:
                happinessList.append(c3happy())
                c3.append(c3happy())

    return sum(happinessList)


def simulation(t, e):

    optimumTotal = 4500

    exploitOnlyExpectedH = 15 + 12 + 10 + (297 * 15)
    exploreOnlyExpectedH = (100 * 10) + (100 * 12) + (100 * 15)
    eGreedyExpectedH = (e *12) + (e*15) + (e*10) + ((100-e)/100) * 300 * 15

    exploitOnlyRegret = optimumTotal - exploitOnlyExpectedH
    exploreOnlyRegret = optimumTotal - exploreOnlyExpectedH
    eGreedyRegret = optimumTotal - eGreedyExpectedH

    exploitave = []
    exploitreg = []
    for i in range(t):
        exploitave.append(exploitOnly())
        exploitreg.append(optimumTotal - exploitOnly())
    exploitAverage = sum(exploitave) / t
    exploitaveregret = sum(exploitreg) / t

    exploreave = []
    explorereg = []
    for i in range(t):
        exploreave.append(exploreOnly())
        explorereg.append(optimumTotal - exploreOnly())
    exploreAverage = sum(exploreave) / t
    exploreaveregret = sum(explorereg) / t

    eGreedyave = []
    eGreedyreg = []
    for i in range(t):
        eGreedyave.append(eGreedy(e))
        eGreedyreg.append(optimumTotal - eGreedy(e))
    eGreedyAverage = sum(eGreedyave) / t
    eGreedyaveregret = sum(eGreedyreg) / t

    d = {"Optimum Hapiness               ": optimumTotal,
         "Exploit Only Expected Happiness": exploitOnlyExpectedH,
         "Explore Only Expected Happiness": exploreOnlyExpectedH,
         "eGreedy Expected Happiness     ": eGreedyExpectedH,
         "Exploit Only Expected Regret   ": exploitOnlyRegret,
         "Explore Only Expected Regret   ": exploreOnlyRegret,
         "eGreedy Expected Regret        ": eGreedyRegret,
         "Exploit Only Average Happiness ": exploitAverage,
         "Explore Only Average Happiness ": exploreAverage,
         "eGreedy Average Happiness      ": eGreedyAverage,
         "Exploit Only Average Regret    ": exploitaveregret,
         "Explore Only Average Regret    ": exploreaveregret,
         "eGreedy Average Regret         ": eGreedyaveregret
         }

    for k, v in d.items():
        print(k, v)
    print("--- end of output ---")
print("This is a simple multi-armed bandit model that will show the expected and actual happiness and regret results from different methods of visitng cafetirias")
x = int(input("Enter number of times you want to visit the cafeterias: "))
print("Enter a number between 0 and 100")
y = int(input("This will be the chances of you going to a random cafeteria in the greedy calculation instead of going to your current happiest one: "))


print (simulation(x, y))
