import requests

# Assume you have a list of plastic waste objects with their coordinates and image URLs
plastic_waste_objects = [
    {"latitude": 51.5074, "longitude": -0.1278, "image_url": "https://example.com/image1.jpg"},
    {"latitude": 40.7128, "longitude": -74.0060, "image_url": "https://example.com/image2.jpg"},
    # Add more plastic waste objects as needed
]

# Loop through the plastic waste objects
for obj in plastic_waste_objects:
    latitude = obj["latitude"]
    longitude = obj["longitude"]
    image_url = obj["image_url"]

    # Geotag the plastic waste by creating a URL with the coordinates
    geotagged_url = f"https://www.google.com/maps?q={latitude},{longitude}"

    # Display the geotagged URL and image URL
    print("Geotagged URL:", geotagged_url)
    print("Image URL:", image_url)
    print()

    # You can also send the geotagged URL and image URL to a database or share them with others
    # Here's an example of sending the URLs to a remote server
    payload = {
        "geotagged_url": geotagged_url,
        "image_url": image_url
    }
    response = requests.post("https://example.com/endpoint", json=payload)
    if response.status_code == 200:
        print("URLs sent successfully!")
    else:
        print("Error occurred while sending URLs.")
