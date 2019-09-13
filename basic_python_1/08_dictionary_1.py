season={1: "Spring is from Jan to Mar",
        2: "Summer is from Apr to June",
        3: "Autumm is from July to Sep",
        4: "Winter is from Oct to Dec",
}

n=int(input("please enter any season from 1~4: "))

if n in season:
    print(season[n])
else:
    print("error input")