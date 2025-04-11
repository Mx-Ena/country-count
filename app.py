from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load the country data
CONTINENT_COUNTRY_MAP = {
    "Africa": ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Comoros", "Congo", "Democratic Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Swaziland", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"],
    "Asia": ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"],
    "Europe": ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"],
    "North America": ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"],
    "Oceania": ["Australia", "Federated States of Micronesia", "Fiji", "Kiribati", "Marshall Islands", "Nauru", "New Zealand", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"],
    "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
}

def generate_output_line(continent):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counts = {letter: 0 for letter in alphabet}
    
    for country in CONTINENT_COUNTRY_MAP[continent]:
        first_letter = country[0].upper()
        if first_letter in counts:
            counts[first_letter] += 1
    
    output_line = ''
    for letter in alphabet:
        count = counts[letter]
        if count == 1:
            output_line += letter
        elif count > 1:
            output_line += f"{letter}{count}"
    
    return output_line

@app.route('/')
def index():
    continent_lines = {}
    continent_counts = {}
    for continent in CONTINENT_COUNTRY_MAP:
        continent_lines[continent] = generate_output_line(continent)
        continent_counts[continent] = len(CONTINENT_COUNTRY_MAP[continent])
    return render_template('index.html', 
                         continent_lines=continent_lines,
                         continent_counts=continent_counts)

@app.route('/get_countries/<continent>/<letter>')
def get_countries(continent, letter):
    matching_countries = [
        country for country in CONTINENT_COUNTRY_MAP[continent]
        if country.upper().startswith(letter.upper())
    ]
    return jsonify(matching_countries)

if __name__ == '__main__':
    app.run(debug=True) 