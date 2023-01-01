import json


def main():
    #get info about animal
    teeth = str(input("How many teeth does your animal have? "))
    wild = str(input("Is the animal wild? "))
    #Find ANimal
    with open("animals.json") as jsonFile:
        data = json.load(jsonFile)
    for e in data:
        #print(e)
        e2 = data[e]
        #print(e2)
        if teeth == e2["teeth"] and wild == e2["wild"]:
            print("Youre thinking of a " + e)


if __name__ == "__main__":
    main()


