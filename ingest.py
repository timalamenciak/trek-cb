from crossref.restful import Works
from teapotai import TeapotAI
from geopy.geocoders import Nominatim
from pdf2image import convert_from_path
import re, csv
import argparse, shutil

#Initialize our tools
works = Works()
teapot_ai = TeapotAI()

#Command-line arguments
args = argparse.ArgumentParser()
args.add_argument("fdoi", help="The DOI of the paper to be ingested.")
args.add_argument("rec", help="The record identifier - journXXXX")
args.add_argument("file", help="The path to the PDF to be ingested.")
values = args.parse_args()

file = values.file
fdoi = values.fdoi
rec = values.rec

#Start building the metadata dict
meta_out = {"objectid": rec,
            "title": None,
            "authorid": None,
            "date": None,
            "journal": None,
            "description": None,
            "subject": None,
            "location": None,
            "latitude": None,
            "longitude": None,
            "source": None,
            "identifier": f"{fdoi}",
            "type": "text",
            "format":"application/pdf",
            "language":"eng",
            "rights": None,
            "rightsstatement": None,
            "display_template": "pdf",
            "object_location": f'/objects/{rec}.pdf',
            "image_small": f'objects/small/{rec}_sm.jpg',
            "image_thumb": f'objects/small/{rec}_sm.jpg',
            "image_alt_text": "An image of the first page of the journal article.",
            "object_transcript": None
            }


#Load metadata from crossref
metad = works.doi(fdoi)
#Check if abstract, if not prompt for it
try:
    abstract = metad['abstract']
    abstract = re.sub(r'<[^>]*?>', '', abstract)
    print("Abstract fetched.")
except KeyError:
    print("Abstract not on CrossRef. Please paste below:")
    abstract = input("Abstract:")

meta_out["description"] = abstract
meta_out["title"] = metad['title'][0]
meta_out["license"] = metad['license'][0]['URL']
meta_out["journal"] = metad['short-container-title']
#Add authors
authors = str()
with open('authors.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    author_data = [row for row in reader]

id = author_data[-1]["objectid"]
for a in metad['author']:
    author = f"{a['given']} {a['family']}"
    try:
        results = [row for row in author_data if 'title' in row and row['title'] == author]
        if results:  # Check if the list is not empty
            authors += f"{results[0]['objectid']};"
        else:
            raise ValueError(f"Author '{author}' not found - adding entry")
    except ValueError as e:
        print(e)
        id = int(id) + 1
        new_author = {"objectid": id,
                      "title": author,
                      "affiliation": a['affiliation'][0]['name'],
                      "orcid": None}
        authors += f"{id};"
        with open('authors.csv', mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=new_author.keys())
            writer.writerow(new_author)

        
meta_out["creator"] = authors

#Add publication date
try: 
    meta_out["date"] = metad['published-print']['date-parts'][0][0]
except KeyError:
    print("Date not in CrossRef. Please enter year of publication")
    meta_out["date"] = input("Year:")

#TeapotAI to extract some stuff from abstract - e.g. location
location_name = teapot_ai.query(
    query="What is the main study location reported in this abstract? Provide the most precise location name reported in the abstract.", 
    context=abstract
)
print(location_name) 

# Initialize Nominatim API
geolocator = Nominatim(user_agent="myGeocoder")

# Geocode a location name
location = geolocator.geocode(location_name)

# Print the coordinates
print((location.latitude, location.longitude))

# Add location and coords to dict
meta_out["location"] = location_name
meta_out["latitude"] = location.latitude
meta_out["longitude"] = location.longitude

#Generate thumbnail from PDF.
#Note that this requires Poppler - a set of external executables.
poppler_path = r"C:/Users/Tim Alamenciak/Documents/Coding/cb_workshop/poppler-24.08.0/Library/bin"
images = convert_from_path(file, dpi=300, poppler_path=poppler_path, first_page=1, last_page=1)
images[0].save(f'objects/small/{rec}_sm.jpg', 'JPEG')
shutil.copy(file, f'objects/{rec}.pdf')

with open('articlemetadata.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(meta_out.values())