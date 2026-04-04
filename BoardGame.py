# Homework 3 - Board Game System
# Name:
# Date:
import random
def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)

def updateHealth(health, event):
    if event == "Heal":
        health += 20
        print("You landed on Heal! Gain 20 health!")
    elif event == "Trap":
        health -= 20
        print("You landed on Trap! Lose 20 health!")
    elif event == "Treasure":
        print("You landed on Treasure! You have good luck!")
    return health

def movePlayer(data, health):
    """Example function to simulate moving a player."""
    for line in data:
        if "Turn" in line:
            parts = line.split(": ")
            player = parts[1]
            data.remove(line)
            break
    move = random.randint(1, 24)
    print(player, "rolled:", move)

    for i in range(len(data)):
        if player in data[i] and ":" in data[i] and "Turn" not in data[i]:
            split = data[i].split(": ")
            newPos = int(split[0]) + move
            data[i] = str(newPos) + ": " + player
            print(player, "moved to", newPos)
        
            if newPos == 12:
                health = updateHealth(health, "Treasure")
            elif newPos == 18:
                health = updateHealth(health, "Trap")
            elif newPos == 27:
                health = updateHealth(health, "Heal")
            break
    return health
    # Students will modify this


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    health = 100
    print("Game is starting! Player1 has 100 health.")
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        health = movePlayer(gameData, health)
        print("Player1 health: " + str(health))
        displayGame(gameData)


if __name__ == "__main__":
    main()
