import requests
import json

#"https://api.nationalize.io/?name=" after '=' you can type the name


name_endpoint = "https://randomuser.me/api/"
user_request = requests.request("GET", name_endpoint)

user_name = json.dumps(user_request.json()["results"][0]["name"]["first"])
user_name = user_name.replace('"', '')


domains = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR", "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE", "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BV", "BR", "IO", "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD", "CL", "CN", "CX", "CC", "CO", "KM", "CD", "CG", "CK", "CR", "CI", "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG", "SV", "GQ", "ER", "EE", "SZ", "ET", "FK", "FO", "FJ", "FI", "FR", "GF", "PR", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD", "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "HM", "VA", "HN", "HK", "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT", "JM", "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG", "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK", "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MY", "YT", "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA", "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP", "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN", "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN", "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC", "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES", "LK", "SD", "SR", "SJ", "SE", "CH", "SY", "TW", "TJ", "TZ", "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV", "UG", "UA", "AE", "GB", "UM", "US", "UY", "UZ", "VU", "VE", "VN", "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
countries = ["Afghanistan", "Åland Islands", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bonaire, Sint Eustatius, Saba", "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo (the Democratic Republic of the Congo)", "Congo", "Cook Islands", "Costa Rica", "Côte d'Ivoire - Ivory Coast", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", " Falkland Islands", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard Island and McDonald Islands", "Holy See", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kuwait", "Kuwait", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "North Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Réunion", "Romania", "Russia", "Rwanda", "Saint Barthélemy", "Saint Helena, Ascencion Island, Tristan da Chunha", "Saint Kitts and Nevis", "Saint Lucia", "Saint Martin", "Saint Pierre and Miquelon", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard, Jan Mayen", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Türkiye", "Turkmenistan", " Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom of Great Britain and Northern Ireland", "United States Minor Outlying Islands", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Viet Nam", "Virgin Islands - British", "Virgin Islands - U.S.", "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"]

guess_nationality_endpoint = "https://api.nationalize.io/?name=" + user_name.lower()
guess_nationality = requests.request("GET", guess_nationality_endpoint)

count = json.dumps(guess_nationality.json()["count"])
name = json.dumps(guess_nationality.json()["name"])

try:
    country_id1 = json.dumps(guess_nationality.json()["country"][0]["country_id"])
except IndexError:
    print("")
    print("A weird name has been created, please retry")
    print("The name that was generated: " + user_name)
    exit()

country_id1 = country_id1.replace('"', '')

country_id2 = json.dumps(guess_nationality.json()["country"][1]["country_id"])
country_id2 = country_id2.replace('"', '')

country_id3 = json.dumps(guess_nationality.json()["country"][2]["country_id"])
country_id3 = country_id3.replace('"', '')

country_id4 = json.dumps(guess_nationality.json()["country"][3]["country_id"])
country_id4 = country_id4.replace('"', '')

country_id5 = json.dumps(guess_nationality.json()["country"][4]["country_id"])
country_id5 = country_id5.replace('"', '')


print("count: " + count)
print("name: " + name)
print("")


user_guess = input("Where do you think this person can be from?(type country's alpha 2 code)")

if user_guess.upper() == country_id1 or user_guess.upper() == country_id2 or user_guess.upper() == country_id3 or user_guess.upper() == country_id4 or user_guess.upper() == country_id5:
    help = -1
    for x in domains:
       help += 1
       if x == user_guess.upper():
          country_name = countries[help]
    
    if country_id1 == user_guess.upper():
      probability = json.dumps(guess_nationality.json()["country"][0]["probability"])

    elif country_id2 == user_guess.upper():
       probability = json.dumps(guess_nationality.json()["country"][1]["probability"])

    elif country_id3 == user_guess.upper():
       probability = json.dumps(guess_nationality.json()["country"][2]["probability"])

    elif country_id4 == user_guess.upper():
       probability = json.dumps(guess_nationality.json()["country"][3]["probability"])

    elif country_id5 == user_guess.upper():
       probability = json.dumps(guess_nationality.json()["country"][4]["probability"])

    print("")
    print("CORRECT")
    print("")

    print("This person can indeed be from " + user_guess.upper() + " - " + country_name)
    print("With the probability of: " + probability)

else:
    help = -1
    for x in domains:
       help += 1
       if x == country_id1:
          country_name1 = countries[help]
    
    help = -1
    for x in domains:
       help += 1
       if x == country_id2:
          country_name2 = countries[help]
    
    help = -1
    for x in domains:
       help += 1
       if x == country_id3:
          country_name3 = countries[help]
    
    help = -1
    for x in domains:
       help += 1
       if x == country_id4:
          country_name4 = countries[help]
    
    help = -1
    for x in domains:
       help += 1
       if x == country_id5:
          country_name5 = countries[help]

    probability1 = json.dumps(guess_nationality.json()["country"][0]["probability"])
    probability2 = json.dumps(guess_nationality.json()["country"][1]["probability"])
    probability3 = json.dumps(guess_nationality.json()["country"][2]["probability"])
    probability4 = json.dumps(guess_nationality.json()["country"][3]["probability"])
    probability5 = json.dumps(guess_nationality.json()["country"][4]["probability"])

    print("")
    print("INCORRECT")
    print("")
    print("This person can be from:")
    print("")

    print(country_name1 + " - " + country_id1)
    print("probability: " + probability1)
    print("")

    print(country_name2 + " - " + country_id2)
    print("probability: " + probability1)
    print("")

    print(country_name3 + " - " + country_id3)
    print("probability: " + probability1)
    print("")

    print(country_name4 + " - " + country_id4)
    print("probability: " + probability1)
    print("")

    print(country_name5 + " - " + country_id5)
    print("probability: " + probability1)
