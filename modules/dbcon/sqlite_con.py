from sqlitedict import SqliteDict

# hiuraroll ownership sqlite database
rollOwnership = SqliteDict("db/rollOwnership.sqlite",
                           tablename="rollOwnership")


# gets ownership status from sqlite database
def get_ownership(user_id, rng, rarity):
    """Returns ownership status"""
    ownership = 0
    for item in rollOwnership.items():
        ownership_info = ("%s=%s" % (item))
        if ((str(user_id) in ownership_info) & (rng in ownership_info)
                & (rarity in ownership_info)):
            ownership = 1
            break
        else:
            ownership = 0
    return ownership


# if not owned, create ownership and commit to database
def make_ownership(user_id, rng, rarity):
    """Creates new ownership"""
    index = len(rollOwnership) + 1
    if get_ownership(user_id, rng, rarity) == 0:
        rollOwnership[index] = {
            "user_id": user_id,
            "image_id": rng,
            "rarity": rarity
        }
        rollOwnership.commit()
        print("Committed new data")
    else:
        print("No commit")
