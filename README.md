# NASA_APOD


## DESCRIPTION:
    Flask server returning Astronomical picture of the day along with the details using
    NASA's APOD API.
    The server created backend for user input(date), filters it and renders accordingly.
    It does not works for fictional dates. 
    Furthurmore, the APOD API only works for dates between 5th June 1995 and present date.

## REQUIREMENTS:
    The following code requires the following packages installed for python3:
    ```
      requests
      flask
    ```
    Furthurmore, the code requires a NASA APOD API which can be easily achieved by signing
    in on their website: https://api.nasa.gov

## USAGE:
    Clone the repository using command:
    ```bash
    $ git clone https://github.com/samsepi0x0/NASA_APOD.git
    ```
    Update the API key in server.py and run the Flask server using commands:
    ```
    $ cd NASA_APOD
    $ nano server.py # update the global variable API with your own API
    $ python server.py
    ```
    Open url: 127.0.0.1:5000 on any browser to see the frontend.
    
    
## OUTPUT:

![Screenshot](https://github.com/samsepi0x0/NASA_APOD/blob/main/screenshots/Screenshot%20from%202021-04-15%2000-17-09.png)

![Screenshot](https://github.com/samsepi0x0/NASA_APOD/blob/main/screenshots/Screenshot%20from%202021-04-15%2000-17-33.png)

