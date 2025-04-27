import os
import re
import time
import requests
from bs4 import BeautifulSoup
import base64

from google import genai
from google.genai import types
import utils

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


def race_url(year, race_id):
    # no logic on which url they use, try both and see which one works
    # Docs only available from 2021 season onwards, 2020 Abu Dhabi unavailable

    import utils

    race_name = utils.get_events(year)[race_id - 1]
    race_name = race_name.replace(" ", "-")
    fia_url1 = f"https://www.fia.com/events/fia-formula-one-world-championship/season-{year}/{race_name}/eventtiming-information"
    fia_url2 = f"https://www.fia.com/events/fia-formula-one-world-championship/season-{year}/{race_name}/eventtiming"

    return fia_url1, fia_url2


def download_lap_chart_pdf(url, year, race_name):
    """
    Download the Lap Chart PDF from the given URL.

    Args:
        url (str): The URL of the FIA event page containing the Lap Chart link
        year (int): The year of the race
        race_name (str): The name of the race

    Returns:
        str: Path to the downloaded PDF file if successful, None otherwise
    """
    try:
        # Fetch the HTML content from the URL
        print(f"Fetching content from: {url}")
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")
            return None

        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all links that might contain PDFs
        links = soup.find_all("a", href=re.compile(r"\.pdf$"))

        # Look for the link with "Lap Chart" text
        lap_chart_link = None
        for link in links:
            # Check if the link text contains "Lap Chart"
            if link.text and "Lap Chart" in link.text:
                lap_chart_link = link["href"]
                break

        # If we couldn't find it by link text, look for divs with "Lap Chart" title
        # that might be near links
        if not lap_chart_link:
            lap_chart_divs = soup.find_all(
                string=lambda text: text and "Lap Chart" in text
            )
            for text in lap_chart_divs:
                # Look for nearby links
                parent = text.parent
                pdf_link = parent.find("a", href=re.compile(r"\.pdf$"))
                if pdf_link:
                    lap_chart_link = pdf_link["href"]
                    break

        # If we still couldn't find it, try to find any div with class "title" containing "Lap Chart"
        if not lap_chart_link:
            title_divs = soup.find_all("div", class_="title")
            for div in title_divs:
                if div.text and "Lap Chart" in div.text:
                    # Look for nearby links
                    parent = div.parent
                    pdf_link = parent.find("a", href=re.compile(r"\.pdf$"))
                    if pdf_link:
                        lap_chart_link = pdf_link["href"]
                        break

        if lap_chart_link:
            # Make sure the URL is absolute
            if not lap_chart_link.startswith(("http://", "https://")):
                # If it's a relative URL, make it absolute
                base_url = "/".join(
                    url.split("/")[:3]
                )  # Get the base URL (e.g., https://www.fia.com)
                if lap_chart_link.startswith("/"):
                    lap_chart_link = base_url + lap_chart_link
                else:
                    lap_chart_link = base_url + "/" + lap_chart_link

            # Download the PDF
            print(f"Downloading Lap Chart PDF from: {lap_chart_link}")
            pdf_response = requests.get(lap_chart_link)

            if pdf_response.status_code == 200:
                # Save the PDF with a more descriptive filename
                filename = f"{year}_{race_name}_lap_chart.pdf"
                with open(filename, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"Successfully downloaded: {os.path.abspath(filename)}")
                return filename
            else:
                print(
                    f"Failed to download PDF. Status code: {pdf_response.status_code}"
                )
                return None
        else:
            print("Could not find a link to the Lap Chart PDF.")

            # As a fallback, print all PDF links found
            print("\nAll PDF links found in the document:")
            for link in links:
                print(f"Text: {link.text.strip() if link.text else 'No text'}")
                print(f"URL: {link['href']}\n")

            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None





def generate_csv_from_pdf(pdf_file, year, race_name):
    """
    Generate a CSV file from a PDF file using Google Gemini API.

    Args:
        pdf_file (str): Path to the PDF file
        year (int): The year of the race
        race_name (str): The name of the race

    Returns:
        str: Path to the generated CSV file
    """
    client = genai.Client(api_key=GEMINI_API_KEY)

    # Ensure the PDF file exists
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file {pdf_file} not found.")
        return None

    # Upload the file
    files = [
        client.files.upload(file=pdf_file),
    ]

    model = "gemini-2.5-pro-exp-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
                types.Part.from_text(
                    text="""Output the data in a csv format

                                     The user wants to extract the table data from the provided image into a CSV format.

1.  **Identify the table:** The image contains a large table titled \"Race Lap Chart\".
2.  **Determine columns:** The columns are labeled \"POS\", \"1\", \"2\", \"3\", ..., \"20\". The \"POS\" column contains lap numbers (\"GRID\", \"LAP 1\", \"LAP 2\", etc.).
3.  **Determine rows:** Each row represents a lap (starting from \"GRID\" which is the starting grid, then \"LAP 1\" ).
4.  **Extract data:** Go through each row, from \"GRID\" , and extract the values for each corresponding position (columns 1 to 20).
5.  **Handle special cases:** Notice the empty cells and cells with boxes around them. The OCR seems to handle them correctly as numbers. The boxes likely indicate pit stops or position changes, but for CSV extraction, just the numbers are needed.
6.  **Format as CSV:** Arrange the extracted data with commas separating the values in each row and a newline character separating the rows. The first row should be the header row (\"POS\", \"1\", \"2\", ..., \"20\").

**Data Extraction Plan:**
- Read the header row: POS, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
- Read GRID row:
- Read LAP 1 row:
- ... and so on for each lap

- Ensure the number of columns matches the header for each row."""
                ),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    # Generate content
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    # Extract CSV content from response
    csv_content = response.text

    csv_content = csv_content.strip()
    if csv_content.startswith("```csv"):
        csv_content = csv_content[6:]  # Remove ```csv
    if csv_content.endswith("```"):
        csv_content = csv_content[:-3]  # Remove ```
    csv_content = csv_content.strip()

    # Save to CSV file
    csv_filename = f"{year}_{race_name}.csv"
    with open(csv_filename, "w", newline="") as csv_file:
        csv_file.write(csv_content)

    print(f"Successfully generated CSV file: {os.path.abspath(csv_filename)}")
    return csv_filename


def process_race_data(year, race_id):
    """
    Process race data by downloading the lap chart PDF and converting it to CSV.

    Args:
        year (int): The year of the race
        race_id (int): The ID of the race

    Returns:
        str: Path to the generated CSV file, or None if processing failed
    """
    

    # Get race name
    race_name = utils.get_events(year)[race_id - 1]
    race_name_formatted = race_name.replace(" ", "_").lower()

    # Get FIA URLs
    fia_url1, fia_url2 = race_url(year, race_id)

    # Try to download the lap chart PDF from the first URL
    pdf_file = download_lap_chart_pdf(fia_url1, year, race_name_formatted)

    # If the first URL failed, try the second URL
    if not pdf_file and fia_url2:
        pdf_file = download_lap_chart_pdf(fia_url2, year, race_name_formatted)

    # If we have a PDF file, generate CSV from it
    if pdf_file:
        return generate_csv_from_pdf(pdf_file, year, race_name_formatted)
    else:
        print(f"Failed to download lap chart PDF for {year} {race_name}")
        return None


if __name__ == "__main__":
    
    years = [2021,2025]
    for year in years:
        try:
            total_races = len(utils.get_events(year))
            for race in range(total_races):                
                csv_file = process_race_data(year, race + 1)              
                print("Waiting 15 seconds before next race...")
                time.sleep(15) # RPM = 5, RPD = 50 for the model
        except Exception as e:
             print(f"An error occurred processing year {year}: {e}")             

    print("\nFinished processing all specified races.")

    
