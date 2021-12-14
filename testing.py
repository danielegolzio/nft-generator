        
def rarity(data):
    number = random.randint(1, 1000)
            
    # 50% chance of getting this rarity
    if number >= 1 and number <= 500:
        rarity = 'common'
        common(data, rarity)
        return rarity
            
    # 25% chance of getting this rarity
    elif number >= 500 and number <= 750:
        rarity = 'uncommon'
        uncommon(data, rarity)
        return rarity

    # 10% chance of getting this rarity
    elif number >= 750 and number <= 850:
        rarity = 'rare'
        rare(data, rarity)
        return rarity

    # 5% chance of getting this rarity
    elif number >= 850 and number <= 900:
        rarity = 'covert'
        covert(data, rarity)
        return rarity

    # 1% chance of getting this rarity
    elif number >= 900 and number <= 910:
        rarity = 'legendary'
        main_colors = 'red'
        legendary_r(data, rarity)
        return rarity

    # 1% chance of getting this rarity
    elif number >= 910 and number <= 920:
        rarity = 'legendary'
        main_colors = 'green'
        legendary_g(data, rarity)
        return rarity

    # 1% chance of getting this rarity
    elif number >= 920 and number <= 930:
        rarity = 'legendary'
        main_colors = 'blue'
        legendary_b(data, rarity)
        return rarity

    # 0.1% chance of getting this rarity
    elif number == 999:
        rarity = 'classified'
        main_colors = 'black'
        classified_blk(data, rarity)
        return rarity

    # 0.1% chance of getting this rarity
    elif number == 1000:
        rarity = 'classified'
        main_colors = 'white'
        classified_wht(data, rarity)
        return rarity