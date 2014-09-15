# /r/AFL Subreddit Flair Statistics

#!/usr/bin/env python
import sys
from datetime import datetime
from praw import Reddit

user = 'rAFLgamethread'
password = 'ENTERPASSWORDHERE'
srname = 'AFL'
edit_reason = 'Updated by /u/rAFLgamethread bot'

r = Reddit('AFL-flairstats/0.1')
r.login(user, password)
sr = r.get_subreddit(srname)

flair_templates = {
    'adelaide': 'Adelaide',
    'adelaide2': 'Adelaide 2',
    'adelaide3': 'Adelaide 3',
    'adelaide5': 'Adelaide 5',
    'brisbane': 'Brisbane',
    'brisbane2': 'Brisbane 2',
    'brisbane3': 'Brisbane 3',
    'brisbane5': 'Brisbane 5',
    'carlton': 'Carlton',
    'carlton2': 'Carlton 2',
    'carlton3': 'Carlton 3',
    'carlton4': 'Carlton 4',
    'collingwood': 'Collingwood',
    'collingwood2': 'Collingwood 2',
    'collingwood3': 'Collingwood 3',
    'collingwood4': 'Collingwood 4',
    'essendon': 'Essendon',
    'essendon2': 'Essendon 2',
    'essendon3': 'Essendon 3',
    'essendon4': 'Essendon 4',
    'fremantle': 'Fremantle',
    'fremantle2': 'Fremantle 2',
    'fremantle3': 'Fremantle 3',
    'fremantle4': 'Fremantle 4',
    'fremantle5': 'Fremantle 5',
    'geelong': 'Geelong',
    'geelong2': 'Geelong 2',
    'geelong3': 'Geelong 3',
    'geelong4': 'Geelong 4',
    'geelong5': 'Geelong 5',
    'goldcoast': 'Gold Coast',
    'goldcoast2': 'Gold Coast 2',
    'goldcoast3': 'Gold Coast 3',
    'greaterwesternsydney': 'Greater Western Sydney',
    'greaterwesternsydney2': 'Greater Western Sydney 2',
    'greaterwesternsydney3': 'Greater Western Sydney 3',
    'hawthorn': 'Hawthorn',
    'hawthorn2': 'Hawthorn 2',
    'hawthorn3': 'Hawthorn 3',
    'hawthorn4': 'Hawthorn 4',
    'hawthorn5': 'Hawthorn 5',
    'melbourne': 'Melbourne',
    'melbourne2': 'Melbourne 2',
    'melbourne3': 'Melbourne 3',
    'melbourne4': 'Melbourne 4',
    'melbourne5': 'Melbourne 5',
    'northmelbourne': 'North Melbourne',
    'northmelbourne2': 'North Melbourne 2',
    'northmelbourne3': 'North Melbourne 3',
    'northmelbourne4': 'North Melbourne 4',
    'northmelbourne5': 'North Melbourne 5',
    'portadelaide': 'Port Adelaide',
    'portadelaide2': 'Port Adelaide 2',
    'portadelaide3': 'Port Adelaide 3',
    'portadelaide4': 'Port Adelaide 4',
    'richmond': 'Richmond',
    'richmond2': 'Richmond 2',
    'richmond3': 'Richmond 3',
    'richmond4': 'Richmond 4',
    'richmond5': 'Richmond 5',
    'stkilda': 'St Kilda',
    'stkilda2': 'St Kilda 2',
    'stkilda3': 'St Kilda 3',
    'stkilda4': 'St Kilda 4',
    'stkilda5': 'St Kilda 5',
    'sydney': 'Sydney',
    'sydney2': 'Sydney 2',
    'sydney3': 'Sydney 3',
    'sydney4': 'Sydney 4',
    'sydney5': 'Sydney 5',
    'westcoast': 'West Coast',
    'westcoast2': 'West Coast 2',
    'westcoast3': 'West Coast 3',
    'westcoast5': 'West Coast 5',
    'westernbulldogs': 'Western Bulldogs',
    'westernbulldogs2': 'Western Bulldogs 2',
    'westernbulldogs3': 'Western Bulldogs 3',
    'westernbulldogs4': 'Western Bulldogs 4',
    'westernbulldogs5': 'Western Bulldogs 5',
    'fitzroy3': 'Fitzroy 3',
    'fitzroy4': 'Fitzroy 4',
    'bears5': 'Bears 5',
    'southaustralia': 'South Australia',
    'tasmania': 'Tasmania',
    'victoria': 'Victoria',
    'westernaustralia': 'Western Australia',
    'allies': 'Allies',
    'university': 'University',
    'canada': 'Canada',
    'china': 'China',
    'fiji': 'Fiji',
    'finland': 'Finland',
    'france': 'France',
    'great-britain': 'Great Britain',
    'india': 'India',
    'indonesia': 'Indonesia',
    'ireland': 'Ireland',
    'japan': 'Japan',
    'nauru': 'Nauru',
    'new-zealand': 'New Zealand',
    'pakistan': 'Pakistan',
    'png': 'Papua New Guinea',
    'south-africa': 'South Africa',
    'sweden': 'Sweden',
    'tonga': 'Tonga',
    'united-states': 'United States',
    'canada-w': 'Canada Womens',
    'tonga-w': 'Tonga Womens',
    'usa-freedom': 'USA Freedom',
    'usa-liberty': 'USA Liberty'    
}

club_templates = {
    'Adelaide',
    'Brisbane',
    'Carlton',
    'Collingwood',
    'Essendon',
    'Fremantle',
    'Geelong',
    'Gold Coast',
    'Greater Western Sydney',
    'Hawthorn',
    'Melbourne',
    'North Melbourne',
    'Richmond',
    'St Kilda',
    'Sydney',
    'West Coast',
    'Western Bulldogs'
}

stats = {}
clubstats = {}
total = 0

# cycle through the user flair list
for item in sr.get_flair_list(limit=9000):
    style = item['flair_css_class']
    if not style:
        continue
    if style not in flair_templates:
        sys.stderr.write("Ignore %s\n" % style)
        continue
    if style in club_templates:
        try:
            clubstats[club_templates.index(style)] +=1
        except KeyError:
            clubstats[club_templates.index(style)] = 1
    try:
        stats[style] += 1
    except KeyError:
        stats[style] = 1
    total += 1

# prepare items
items = stats.items()
items.sort(lambda x,y: cmp(y[1], x[1]))
stats = []
clubitems = clubstats.items()
clubitems.sort(lambda x,y: cmp(y[1], x[1]))
clubstats = []

# append to output
for style, count in items:
    stats.append("    %5d (%5.1f%%) %s" % (count, float(count*100.0)/total, flair_templates[style]))
stats.append("    %5d (100.0%%) %s" % (total, "Total"))
stats.append("*Updated %s*" % datetime.utcnow().strftime("%Y-%m-%d %H:%MZ"))

# append club totals to output
for style, count in clubitems:
    clubstats.append("    %5d (%5.1f%%) Total Club Flair - %s" % (count, float(count*100.0)/total, flair_templates[style]))
clubstats.append("    %5d (100.0%%) %s" % (total, "Total"))
clubstats.append("*Updated %s*" % datetime.utcnow().strftime("%Y-%m-%d %H:%MZ"))

# print console output
output = '\n'.join(stats)
output_clubs = '\n'.join(clubstats)
output_final = output + '\n\n\n' + output_clubs
print(output_final)

# write to wiki page
sr.edit_wiki_page('flair_stats', output_final, reason=edit_reason)
