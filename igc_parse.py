from datetime import date, time, timezone
from pprint import pprint


class Flight:
    def __init__(self, filename):
        self.filename = filename

        try:
            self.earth_model = "WGS84"
            self.nav_data = []

            with open(filename, "r") as f:
                for line in f:
                    if "HFPLTPILOTINCHARGE" in line:
                        self.pilot = line[19:].strip()
                    elif "HFGTYGLIDERTYPE" in line:
                        # Glider type
                        self.glider_type = line[16:].strip()
                    elif "HOSITSite" in line:
                        # Site of flight
                        self.flight_site = line[10:].strip()
                    elif "HFDTEDATE" in line:
                        # Date of flight
                        raw = line[10:].strip().split(",")
                        self.flight_date = date(
                            int("20" + raw[0][4:6]),
                            int(raw[0][2:4]),
                            int(raw[0][0:2]),
                        )
                        self.flight_num = raw[1]
                    elif line[0] == "B":
                        # flight data entry
                        self.nav_data.append(
                            {
                                "time": time(
                                    int(line[1:3]),
                                    int(line[3:5]),
                                    int(line[5:7]),
                                ),
                                "lat": line[7:15],
                                "lon": line[15:24],
                                "Fix Validity": line[24:25],
                                "Pressure Altitude": int(line[25:30]),
                                "GPS Altitude": int(line[30:35]),
                            }
                        )
        except IOError:
            print("Error: File not found")


a = Flight(
    "D:/Users/Christian/Study/Year 5/Semester 1/flights/Andrew Tracey-Smith - 23.1.2022.igc"
)
print(a.pilot)
print(a.glider_type)
print(a.flight_site)
print(a.flight_date)
pprint(a.nav_data)
