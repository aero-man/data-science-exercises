'''
Clean the file of MoMA artworks and their artists/dates.

Original artworks.csv has the following columns:
    Title
    Artist
    Nationality
    BeginDate
    EndDate
    Gender
    Date
    Department
Cleaned output CSV has the following columns:
    title
    artist
    nationality
    gender
    artist_birth_date
    artist_death_date
    artwork_begin_date
    artwork_end_date
    moma_department
'''

import csv


def format_nationality(nationality):
    # Convert `(American)` to `American`
    if not nationality:
        return None
    else:
        return nationality.replace("(","").replace(")","").title()

def format_gender(gender):
    # Convert `(Male)` or `` to `Male`, `Female`, or `Other/Unknown`
    if not gender or gender == "" or gender == "()" or len(gender) < 1:
        formatted_gender = "Other/Unknown"
    else:
        formatted_gender = gender.replace("(","").replace(")","").title()
    return formatted_gender

def format_year(year):
    # Convert `(1900)` to `1900`
    if not year:
        return None
    else:
        stripped_year = remove_bad_chars(year)
        formatted_year = int(stripped_year)
        return formatted_year

def format_year_range(years):
    # Convert `(1900-1950)` or `c. 1900-1950` to [1900, 1950]
    year_string = remove_bad_chars(years)
    year_range = year_string.split("-")
    return [int(year) for year in year_range]

def remove_bad_chars(year):
    # Remove unwanted chars from year columns (EX: `(c. 1950)`)
    bad_chars = ["(",")","c","C",".","s","'", " "]
    for char in bad_chars:
        year = year.replace(char, "")
    return year

def split_year_range(years):
    # Convert `1900-1950` to [1900, 1950]
    years = years.replace("(","").replace(")","")
    years = years.split("-")
    return [int(years[0]), int(years[1])]


def main():
    infile = 'artworks.csv'
    outfile = 'artworks_clean.csv'

    artworks_infile = list(csv.reader(open(infile)))
    artworks_clean_outfile = csv.writer(open(outfile, 'w'))

    clean_header = [ # New header for cleaned columns
        'title',
        'artist',
        'nationality',
        'gender',
        'artist_birth_date',
        'artist_death_date',
        'artwork_begin_date',
        'artwork_end_date',
        'moma_department'
    ]
    artworks_clean.writerow(clean_header)

    # Clean each row and write to new CSV
    for artwork in artworks[1:]:
        clean_artwork = []
        clean_artwork.append(artwork[0])
        clean_artwork.append(artwork[1])
        clean_artwork.append(format_nationality(artwork[2]))
        clean_artwork.append(format_gender(artwork[5]))
        clean_artwork.append(format_year(artwork[3]))
        clean_artwork.append(format_year(artwork[4]))
        if "-" in artwork[6]: # EX: `1900-1950`
            year_range = format_year_range(artwork[6])
            clean_artwork.extend(year_range)
        else: # Make start and end date equal to the same year
            formatted_year = format_year(artwork[6])
            clean_artwork.extend([formatted_year, formatted_year])
        clean_artwork.append(artwork[7])

        artworks_clean.writerow(clean_artwork)


if __name__ == "__main__":
    main()

