'''discord bot created using the discord.py library'''
import requests

#--------------API INITIAL/ENDPOINTS---------------------
CLAN_RESPONSE = requests.get('http://api.cr-api.com/clan/2GG9CC', timeout=5.000)
CLAN_RESPONSE = CLAN_RESPONSE.json()
CLAN_MEMBERS = CLAN_RESPONSE['members']

# -----------------------------------------

def getmember(membername: str):
    '''Gets member data from given membername'''
    baseurl = 'http://api.cr-api.com/profile/'
    tag = ""
    url = ""
    for member in CLAN_MEMBERS:
        if member['name'] == membername:
            tag = member['tag']
            url = baseurl+tag
            print("Member found: " + membername + " " + "Tag: " + tag)

    memberdata = requests.get(url, timeout=5.000)
    memberdata = memberdata.json()
    experience = memberdata['experience']
    stats = memberdata["stats"]
    games = memberdata["games"]

    print(
        'Name: ' + memberdata["name"] + "\n" +
        'Current Trophies: ' + str(memberdata["trophies"]) + "\n" +
        'Current Level: ' + str(experience["level"]) + "\n" +
        '----Statistics----\n' +
        'Legendary Trophies: ' + str(memberdata["legendaryTrophies"]) + "\n" +
        'Highest Trophy Count: ' + str(stats["maxTrophies"]) + "\n" +
        'Three Crown Wins: ' + str(stats["threeCrownWins"]) + "\n" +
        'Favorite card: ' + stats["favoriteCard"] + "\n" +
        'Total donations: ' + str(stats["totalDonations"]) + "\n" +
        'Win-Loss-Draw Record: ' + str(games["wins"]) + "-" + str(games["losses"]) + "-" + str(games["draws"])
    )

def main():
    '''I hate python'''
    getmember("bigboi")

if __name__ == '__main__':
    main()
