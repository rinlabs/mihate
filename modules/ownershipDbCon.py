from sqlitedict import SqliteDict

#hiuraroll ownership sqlite database
rollOwnership = SqliteDict("rollOwnership.sqlite",tablename = "rollOwnership")

# gets ownership status from sqlite database
def getOwnership(userID,RNG,rarity):
    ownership=0
    for item in rollOwnership.items():
        ownershipInfo = ("%s=%s" % (item))
        if((str(userID) in ownershipInfo) & \
            (RNG in ownershipInfo)  & \
            (rarity in ownershipInfo)):
            ownership =  1
            break
        else:
            ownership =  0
    return ownership

# if not owned, create ownership and commit to database
def makeOwnership(userID,RNG,rarity):
    index = len(rollOwnership)+1
    if (getOwnership(userID,RNG,rarity) == 0):
        rollOwnership[index] = {"user_id":userID,"image_id":RNG,"rarity":rarity}
        rollOwnership.commit()
    else:
        print(getOwnership(userID,RNG,rarity))
