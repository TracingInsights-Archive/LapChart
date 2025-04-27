import datetime
import json
import os

import matplotlib as mpl
import requests
import wget
from matplotlib.font_manager import FontProperties


def get_custom_font(url, font_filename=None):
    # Extract filename from URL if not provided
    if font_filename is None:
        font_filename = os.path.basename(url)

    # Check if the font file already exists in the current directory
    if os.path.exists(font_filename):
        print(f"Using existing font file: {font_filename}")
    else:
        print(f"Downloading font file: {font_filename}")
        wget.download(url)
        print()  # Add a newline after wget's progress bar

    return FontProperties(fname=font_filename)


def setup_plot_style(background="lightblue", text_color="black"):
    """Configure matplotlib styling for the plot."""
    mpl.rcParams["xtick.color"] = text_color
    mpl.rcParams["ytick.color"] = text_color
    mpl.rcParams["xtick.labelsize"] = 32
    mpl.rcParams["ytick.labelsize"] = 32
    mpl.rcParams["axes.labelcolor"] = text_color
    mpl.rcParams["figure.facecolor"] = background
    mpl.rcParams["axes.facecolor"] = background

    # Configure spines
    mpl.rcParams["axes.spines.top"] = False
    mpl.rcParams["axes.spines.right"] = False
    mpl.rcParams["axes.spines.left"] = True
    mpl.rcParams["axes.spines.bottom"] = True
    mpl.rcParams["axes.edgecolor"] = text_color

    # Configure legend
    mpl.rcParams["legend.frameon"] = True
    mpl.rcParams["legend.facecolor"] = background
    mpl.rcParams["legend.edgecolor"] = text_color
    mpl.rcParams["legend.fancybox"] = True
    mpl.rcParams["legend.fontsize"] = 32

    # Configure other text elements
    mpl.rcParams["axes.titlesize"] = 32
    mpl.rcParams["axes.labelsize"] = 32
    mpl.rcParams["ytick.major.size"] = 0


def get_years():
    """Get a list of available years for the race starting from current year to 2018."""
    current_year = datetime.datetime.now().year
    years = list(range(current_year, 2017, -1))

    return years


def get_events(year):
    events = {
        2025: [
            # "Australian Grand Prix",
            "Chinese Grand Prix",
            "Japanese Grand Prix",
            "Bahrain Grand Prix",
            "Saudi Arabian Grand Prix",
            # "Miami Grand Prix",
            # "Emilia Romagna Grand Prix",
            # "Monaco Grand Prix",
            # "Spanish Grand Prix",
            # "Canadian Grand Prix",
            # "Austrian Grand Prix",
            # "British Grand Prix",
            # "Belgian Grand Prix",
            # "Hungarian Grand Prix",
            # "Dutch Grand Prix",
            # "Italian Grand Prix",
            # "Azerbaijan Grand Prix",
            # "Singapore Grand Prix",
            # "United States Grand Prix",
            # "Mexico City Grand Prix",
            # "São Paulo Grand Prix",
            # "Las Vegas Grand Prix",
            # "Qatar Grand Prix",
            # "Abu Dhabi Grand Prix",
            
        ],
        2024: [
            "Bahrain Grand Prix",
            "Saudi Arabian Grand Prix",
            "Australian Grand Prix",
            "Japanese Grand Prix",
            "Chinese Grand Prix",
            "Miami Grand Prix",
            "Emilia Romagna Grand Prix",
            "Monaco Grand Prix",
            "Canadian Grand Prix",
            "Spanish Grand Prix",
            "Austrian Grand Prix",
            "British Grand Prix",
            "Hungarian Grand Prix",
            "Belgian Grand Prix",
            "Dutch Grand Prix",
            "Italian Grand Prix",
            "Azerbaijan Grand Prix",
            "Singapore Grand Prix",
            "United States Grand Prix",
            "Mexico City Grand Prix",
            "São Paulo Grand Prix",
            "Las Vegas Grand Prix",
            "Qatar Grand Prix",
            "Abu Dhabi Grand Prix",
            
        ],
        2023: [
            "Abu Dhabi Grand Prix",
            "Las Vegas Grand Prix",
            "São Paulo Grand Prix",
            "Mexico City Grand Prix",
            "United States Grand Prix",
            "Qatar Grand Prix",
            "Japanese Grand Prix",
            "Singapore Grand Prix",
            "Italian Grand Prix",
            "Dutch Grand Prix",
            "Belgian Grand Prix",
            "Hungarian Grand Prix",
            "British Grand Prix",
            "Austrian Grand Prix",
            "Canadian Grand Prix",
            "Spanish Grand Prix",
            "Monaco Grand Prix",
            "Miami Grand Prix",
            "Azerbaijan Grand Prix",
            "Australian Grand Prix",
            "Saudi Arabian Grand Prix",
            "Bahrain Grand Prix",
            
        ],
        2022: [
            "Abu Dhabi Grand Prix",
            "São Paulo Grand Prix",
            "Mexico City Grand Prix",
            "United States Grand Prix",
            "Japanese Grand Prix",
            "Singapore Grand Prix",
            "Italian Grand Prix",
            "Dutch Grand Prix",
            "Belgian Grand Prix",
            "Hungarian Grand Prix",
            "French Grand Prix",
            "Austrian Grand Prix",
            "British Grand Prix",
            "Canadian Grand Prix",
            "Azerbaijan Grand Prix",
            "Monaco Grand Prix",
            "Spanish Grand Prix",
            "Miami Grand Prix",
            "Emilia Romagna Grand Prix",
            "Australian Grand Prix",
            "Saudi Arabian Grand Prix",
            "Bahrain Grand Prix",
            
        ],
        2021: [
            "Abu Dhabi Grand Prix",
            "Saudi Arabian Grand Prix",
            "Qatar Grand Prix",
            "São Paulo Grand Prix",
            "Mexico City Grand Prix",
            "United States Grand Prix",
            "Turkish Grand Prix",
            "Russian Grand Prix",
            "Italian Grand Prix",
            "Dutch Grand Prix",
            "Belgian Grand Prix",
            "Hungarian Grand Prix",
            "British Grand Prix",
            "Austrian Grand Prix",
            "Styrian Grand Prix",
            "French Grand Prix",
            "Azerbaijan Grand Prix",
            "Monaco Grand Prix",
            "Spanish Grand Prix",
            "Portuguese Grand Prix",
            "Emilia Romagna Grand Prix",
            "Bahrain Grand Prix",
        ],
        2020: [
            "Abu Dhabi Grand Prix",
            "Sakhir Grand Prix",
            "Bahrain Grand Prix",
            "Turkish Grand Prix",
            "Emilia Romagna Grand Prix",
            "Portuguese Grand Prix",
            "Eifel Grand Prix",
            "Russian Grand Prix",
            "Tuscan Grand Prix",
            "Italian Grand Prix",
            "Belgian Grand Prix",
            "Spanish Grand Prix",
            "70th Anniversary Grand Prix",
            "British Grand Prix",
            "Hungarian Grand Prix",
            "Styrian Grand Prix",
            "Austrian Grand Prix",
        ],
        2019: [
            "Abu Dhabi Grand Prix",
            "Brazilian Grand Prix",
            "United States Grand Prix",
            "Mexican Grand Prix",
            "Japanese Grand Prix",
            "Russian Grand Prix",
            "Singapore Grand Prix",
            "Italian Grand Prix",
            "Belgian Grand Prix",
            "Hungarian Grand Prix",
            "German Grand Prix",
            "British Grand Prix",
            "Austrian Grand Prix",
            "French Grand Prix",
            "Canadian Grand Prix",
            "Monaco Grand Prix",
            "Spanish Grand Prix",
            "Azerbaijan Grand Prix",
            "Chinese Grand Prix",
            "Bahrain Grand Prix",
            "Australian Grand Prix",
        ],
        2018: [
            "Abu Dhabi Grand Prix",
            "Brazilian Grand Prix",
            "Mexican Grand Prix",
            "United States Grand Prix",
            "Japanese Grand Prix",
            "Russian Grand Prix",
            "Singapore Grand Prix",
            "Italian Grand Prix",
            "Belgian Grand Prix",
            "Hungarian Grand Prix",
            "German Grand Prix",
            "British Grand Prix",
            "Austrian Grand Prix",
            "French Grand Prix",
            "Canadian Grand Prix",
            "Monaco Grand Prix",
            "Spanish Grand Prix",
            "Azerbaijan Grand Prix",
            "Chinese Grand Prix",
            "Bahrain Grand Prix",
            "Australian Grand Prix",
        ],
    }

    return events.get(year, [])


def get_sessions(year, event):
    p1_p2_p3 = ["Practice 1", "Practice 2", "Practice 3"]
    p1_p2_q_r = ["Practice 1", "Practice 2", "Qualifying", "Race"]
    p2_p3_q_r = ["Practice 2", "Practice 3", "Qualifying", "Race"]
    p3_q_r = ["Practice 3", "Qualifying", "Race"]
    p1_q_r = ["Practice 1", "Qualifying", "Race"]
    normal_sessions = [
        "Practice 1",
        "Practice 2",
        "Practice 3",
        "Qualifying",
        "Race",
    ]

    normal_sprint = [
        "Practice 1",
        "Qualifying",
        "Practice 2",
        "Sprint Qualifying",
        "Race",
    ]
    sprint_2022 = [
        "Practice 1",
        "Qualifying",
        "Practice 2",
        "Sprint",
        "Race",
    ]

    sprint_shootout = [
        "Practice 1",
        "Qualifying",
        "Sprint Shootout",
        "Sprint",
        "Race",
    ]
    sprint_shootout_2024 = [
        "Practice 1",
        "Sprint Shootout",
        "Sprint",
        "Qualifying",
        "Race",
    ]

    if year == 2018:
        return normal_sessions
    if year == 2019:
        if event == "Japanese Grand Prix":
            return p1_p2_q_r
        return normal_sessions
    if year == 2020:
        if event == "Styrian Grand Prix":
            return p1_p2_q_r
        if event == "Eifel Grand Prix":
            return p3_q_r
        if event == "Emilia Romagna Grand Prix":
            return p1_q_r

        return normal_sessions
    if year == 2021:
        if (
            event == "British Grand Prix"
            or event == "Italian Grand Prix"
            or event == "São Paulo Grand Prix"
        ):
            return normal_sprint
        else:
            return normal_sessions

    if year == 2022:
        if event == "Pre-Season Test":
            return p1_p2_p3
        if (
            event == "Austrian Grand Prix"
            or event == "Emilia Romagna Grand Prix"
            or event == "São Paulo Grand Prix"
        ):
            return sprint_2022
        else:
            return normal_sessions

    if year == 2023:
        if event == "Pre-Season Testing":
            return p1_p2_p3
        if event == "Hungarian Grand Prix":
            return p2_p3_q_r
        if (
            event == "Austrian Grand Prix"
            or event == "Azerbaijan Grand Prix"
            or event == "Belgium Grand Prix"
            or event == "Qatar Grand Prix"
            or event == "United States Grand Prix"
            or event == "São Paulo Grand Prix"
        ):
            return sprint_shootout
        else:
            return normal_sessions
    if year == 2024:
        if event == "Pre-Season Testing":
            return p1_p2_p3
        if (
            event == "Chinese Grand Prix"
            or event == "Miami Grand Prix"
            or event == "Austrian Grand Prix"
            or event == "United States Grand Prix"
            or event == "São Paulo Grand Prix"
            or event == "Qatar Grand Prix"
        ):
            return sprint_shootout_2024

        return normal_sessions
    if year == 2025:
        if event == "Pre-Season Testing":
            return p1_p2_p3
        if (
            event == "Chinese Grand Prix"
            or event == "Miami Grand Prix"
            or event == "Belgium Grand Prix"
            or event == "United States Grand Prix"
            or event == "São Paulo Grand Prix"
            or event == "Qatar Grand Prix"
        ):
            return sprint_shootout_2024

        return normal_sessions


# make sure that year can be from 2018 to current year
class LatestData:

    def __init__(self, year):

        self.year = year
        self.data = self.get_f1_data()
        self.events = self.get_events()

    def get_f1_data(self):
        response = requests.get(
            f"https://livetiming.formula1.com/static/{self.year}/Index.json", timeout=5
        )
        if response.status_code == 200:
            try:
                data = response.content.decode("utf-8-sig")
                return json.loads(data)
            except json.JSONDecodeError as e:
                print("Failed to parse JSON data:", e)
                return None
        else:
            print("Failed to get data. Status code:", response.status_code)
            return None

    def get_events(self):
        events = []
        for meeting in self.data["Meetings"]:
            events.append(meeting["Name"])

        return events

    def get_sessions(self, event):
        sessions = []
        for meeting in self.data["Meetings"]:
            if meeting["Name"] == event:
                for session in meeting["Sessions"]:
                    sessions.append(session["Name"])

        return sessions


def team_codes(year: int) -> dict:
    team_codes = {}
    if year == 2025:
        team_codes = {
            "Red Bull Racing": "RBR",
            "Ferrari": "FER",
            "Aston Martin": "AMR",
            "Mercedes": "MER",
            "Alpine": "APN",
            "Haas F1 Team": "HAA",
            "McLaren": "MCL",
            "Kick Sauber": "KS",
            "Racing Bulls": "RB",
            "Williams": "WIL",
            "Red Bull Racing Honda RBPT": "RBR",
            "Aston Martin Aramco Mercedes": "AMR",
            "Racing Bulls Honda RBPT": "RB",
            "Alpine Renault": "APN",
            "Haas Ferrari": "HAA",
            "McLaren Mercedes": "MCL",
            "Kick Sauber Ferrari": "KS",
            "Williams Mercedes": "WIL",
            "Red Bull": "RBR",
            "Alpine F1 Team": "APN",
        }

    if year == 2024:
        team_codes = {
            "Red Bull Racing": "RBR",
            "Ferrari": "FER",
            "Aston Martin": "AMR",
            "Mercedes": "MER",
            "Alpine": "APN",
            "Haas F1 Team": "HAA",
            "McLaren": "MCL",
            "Kick Sauber": "KS",
            "RB": "RB",
            "Williams": "WIL",
            "Red Bull Racing Honda RBPT": "RBR",
            "Ferrari": "FER",
            "Aston Martin Aramco Mercedes": "AMR",
            "Mercedes": "MER",
            "Alpine Renault": "APN",
            "Haas Ferrari": "HAA",
            "McLaren Mercedes": "MCL",
            "Alfa Romeo Ferrari": "KS",
            "AlphaTauri Honda RBPT": "RB",
            "Williams Mercedes": "WIL",
            "Red Bull": "RBR",
            "Alpine F1 Team": "APN",
        }

    if year == 2023:
        team_codes = {
            "Red Bull Racing": "RBR",
            "Ferrari": "FER",
            "Aston Martin": "AMR",
            "Mercedes": "MER",
            "Alpine": "APN",
            "Haas F1 Team": "HAA",
            "McLaren": "MCL",
            "Alfa Romeo": "ARR",
            "AlphaTauri": "APT",
            "Williams": "WIL",
            "Red Bull Racing Honda RBPT": "RBR",
            "Ferrari": "FER",
            "Aston Martin Aramco Mercedes": "AMR",
            "Mercedes": "MER",
            "Alpine Renault": "APN",
            "Haas Ferrari": "HAA",
            "McLaren Mercedes": "MCL",
            "Alfa Romeo Ferrari": "ARR",
            "AlphaTauri Honda RBPT": "APT",
            "Williams Mercedes": "WIL",
            "Red Bull": "RBR",
            "Alpine F1 Team": "APN",
        }
    if year == 2022:

        team_codes = {
            "Red Bull Racing": "RBR",
            "Ferrari": "FER",
            "Aston Martin": "AMR",
            "Mercedes": "MER",
            "Alpine": "APN",
            "Haas F1 Team": "HAA",
            "McLaren": "MCL",
            "Alfa Romeo": "ARR",
            "AlphaTauri": "APT",
            "Williams": "WIL",
            "Red Bull": "RBR",
            "Alpine F1 Team": "APN",
        }

    if year == 2021:

        team_codes = {
            "Red Bull Racing": "RBR",
            "Mercedes": "MER",
            "Ferrari": "FER",
            "Alpine": "APN",
            "McLaren": "MCL",
            "Alfa Romeo Racing": "ARR",
            "Aston Martin": "AMR",
            "Haas F1 Team": "HAA",
            "AlphaTauri": "APT",
            "Williams": "WIL",
            "Red Bull": "RBR",
            "Alpine F1 Team": "APN",
            "Alfa Romeo": "ARR",
        }

    if year == 2020:

        team_codes = {
            "Red Bull Racing": "RBR",
            "Renault": "REN",
            "Racing Point": "RP",
            "Mercedes": "MER",
            "Ferrari": "FER",
            "McLaren": "MCL",
            "Alfa Romeo Racing": "ARR",
            "Haas F1 Team": "HAA",
            "AlphaTauri": "APT",
            "Williams": "WIL",
            "Red Bull": "RBR",
            "Alfa Romeo": "ARR",
        }

    if year == 2019:

        team_codes = {
            "Red Bull Racing": "RBR",
            "Renault": "REN",
            "Racing Point": "RP",
            "Toro Rosso": "TR",
            "Mercedes": "MER",
            "Ferrari": "FER",
            "McLaren": "MCL",
            "Alfa Romeo Racing": "ARR",
            "Haas F1 Team": "HAA",
            "Williams": "WIL",
            "Red Bull": "RBR",
            "Alfa Romeo": "ARR",
        }

    if year == 2018:

        team_codes = {
            "Red Bull Racing": "RBR",
            "Renault": "REN",
            "Toro Rosso": "TR",
            "Force India": "FI",
            "Sauber": "SB",
            "Mercedes": "MER",
            "Ferrari": "FER",
            "McLaren": "MCL",
            "Haas F1 Team": "HAA",
            "Williams": "WIL",
            "Red Bull": "RBR",
        }

    return team_codes


def team_colors(year: int) -> dict:
    team_colors = {}

    if year == 2025:
        team_colors = {
            "Red Bull Racing": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine": "#f032e6",
            "Haas F1 Team": "#ffffff",
            "McLaren": "#f58231",
            "Kick Sauber": "#00ff00",
            "Racing Bulls": "#dcbeff",
            "Williams": "#4363d8",
            "Red Bull Racing Honda RBPT": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin Aramco Mercedes": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine Renault": "#f032e6",
            "Haas Ferrari": "#ffffff",
            "McLaren Mercedes": "#f58231",
            "Kick Sauber Ferrari": "#00ff00",
            "Alfa Romeo Ferrari": "#800000",
            "Racing Bulls Honda RBPT": "#dcbeff",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6",
        }

    if year == 2024:
        team_colors = {
            "Red Bull Racing": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine": "#f032e6",
            "Haas F1 Team": "#ffffff",
            "McLaren": "#f58231",
            "Kick Sauber": "#00ff00",
            "Kick Sauber Ferrari": "#00ff00",
            "RB": "#dcbeff",
            "Williams": "#4363d8",
            "Red Bull Racing Honda RBPT": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin Aramco Mercedes": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine Renault": "#f032e6",
            "Haas Ferrari": "#ffffff",
            "McLaren Mercedes": "#f58231",
            "Alfa Romeo Ferrari": "#800000",
            "AlphaTauri Honda RBPT": "#dcbeff",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6",
            "RB Honda RBPT": "#dcbeff",
        }

    if year == 2023:
        team_colors = {
            "Red Bull Racing": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine": "#f032e6",
            "Haas F1 Team": "#ffffff",
            "McLaren": "#f58231",
            "Alfa Romeo": "#800000",
            "AlphaTauri": "#dcbeff",
            "Williams": "#4363d8",
            "Red Bull Racing Honda RBPT": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin Aramco Mercedes": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine Renault": "#f032e6",
            "Haas Ferrari": "#ffffff",
            "McLaren Mercedes": "#f58231",
            "Alfa Romeo Ferrari": "#800000",
            "AlphaTauri Honda RBPT": "#dcbeff",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6",
        }
    if year == 2022:

        team_colors = {
            "Red Bull Racing": "#ffe119",
            "Red Bull Racing RBPT": "#ffe119",
            "Ferrari": "#e6194b",
            "Aston Martin": "#3cb44b",
            "Aston Martin Aramco Mercedes": "#3cb44b",
            "Mercedes": "#00c0bf",
            "Alpine": "#f032e6",
            "Haas F1 Team": "#ffffff",
            "Haas Ferrari": "#ffffff",
            "McLaren": "#f58231",
            "McLaren Mercedes": "#f58231",
            "Alfa Romeo": "#800000",
            "Alfa Romeo Ferrari": "#800000",
            "AlphaTauri": "#dcbeff",
            "AlphaTauri RBPT": "#dcbeff",
            "Williams": "#4363d8",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6",
            "Alpine Renault": "#f032e6",
        }

    if year == 2021:

        team_colors = {
            "Red Bull Racing": "#ffe119",
            "Red Bull Racing Honda": "#ffe119",
            "Mercedes": "#00c0bf",
            "Ferrari": "#e6194b",
            "Alpine": "#f032e6",
            "Alpine Renault": "#f032e6",
            "McLaren": "#f58231",
            "McLaren Mercedes": "#f58231",
            "Alfa Romeo Racing": "#800000",
            "Aston Martin": "#3cb44b",
            "Aston Martin Mercedes": "#3cb44b",
            "Haas F1 Team": "#ffffff",
            "Haas Ferrari": "#ffffff",
            "AlphaTauri": "#dcbeff",
            "AlphaTauri Honda": "#dcbeff",
            "Williams": "#4363d8",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#ffe119",
            "Alpine F1 Team": "#f032e6",
            "Alfa Romeo": "#800000",
            "Alfa Romeo Racing Ferrari": "#800000",
        }

    if year == 2020:

        team_colors = {
            "Red Bull Racing": "#000099",
            "Red Bull Racing Honda": "#000099",
            "Renault": "#ffe119",
            "Racing Point": "#f032e6",
            "Racing Point BWT Mercedes": "#f032e6",
            "Mercedes": "#00c0bf",
            "Ferrari": "#e6194b",
            "McLaren": "#f58231",
            "McLaren Renault": "#f58231",
            "Alfa Romeo Racing": "#800000",
            "Alfa Romeo Racing Ferrari": "#800000",
            "Haas F1 Team": "#ffffff",
            "Haas Ferrari": "#ffffff",
            "AlphaTauri": "#dcbeff",
            "AlphaTauri Honda": "#dcbeff",
            "Williams": "#4363d8",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#000099",
            "Alfa Romeo": "#800000",
        }

    if year == 2019:

        team_colors = {
            "Red Bull Racing": "#000099",
            "Red Bull Racing Honda": "#000099",
            "Renault": "#ffe119",
            "Racing Point": "#f032e6",
            "Racing Point BWT Mercedes": "#f032e6",
            "Toro Rosso": "#dcbeff",
            "Scuderia Toro Rosso Honda": "#dcbeff",
            "Mercedes": "#00c0bf",
            "Ferrari": "#e6194b",
            "McLaren": "#f58231",
            "McLaren Renault": "#f58231",
            "Alfa Romeo Racing": "#800000",
            "Alfa Romeo Racing Ferrari": "#800000",
            "Haas F1 Team": "#ffffff",
            "Haas Ferrari": "#ffffff",
            "Williams": "#4363d8",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#000099",
            "Alfa Romeo": "#800000",
        }

    if year == 2018:

        team_colors = {
            "Red Bull Racing": "#000099",
            "Red Bull Racing TAG Heuer": "#000099",
            "Renault": "#ffe119",
            "Toro Rosso": "#dcbeff",
            "Scuderia Toro Rosso Honda": "#dcbeff",
            "Force India": "#f032e6",
            "Force India Sahara": "#f032e6",
            "Force India Mercedes": "#f032e6",
            "Sauber": "#800000",
            "Sauber Ferrari": "#800000",
            "Mercedes": "#00c0bf",
            "Ferrari": "#e6194b",
            "McLaren": "#f58231",
            "McLaren Renault": "#f58231",
            "Haas F1 Team": "#ffffff",
            "Haas Ferrari": "#ffffff",
            "Williams": "#4363d8",
            "Williams Mercedes": "#4363d8",
            "Red Bull": "#000099",
        }

    return team_colors
