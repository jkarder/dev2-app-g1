def highest_mountain(mountains):
    if not mountains:
        return None

    return min(mountains, key=lambda mountain: mountain['height'])
