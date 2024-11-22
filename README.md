# URL_SHORTENER

This is a simple web application built with Streamlit that allows users to shorten URLs using the TinyURL service.

## Features

- Input a long URL and get a shortened version instantly.
- Built with a clean and intuitive interface using Streamlit.
- Uses the `pyshorteners` library to integrate with TinyURL.

## Installation

To run this application locally, follow the steps below:

### Prerequisites

- Python 3.7 or higher installed on your system.
- Ensure `pip` is installed and updated.

### Steps

1. Clone the repository:

   ```bash
   git clone -b master <repository_url>
   cd <repository_name>
   ```
2. Install the required dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
     streamlit run app.py
   ```

## Requirements

This application requires the following Python packages:

- `streamlit`: For building the web interface.
- `pyshorteners`: For shortening URLs using TinyURL.

These dependencies are listed in `requirements.txt`.

## Usage
Enter the URL you wish to shorten in the input field displayed on the app.
Click the "Shorten" button.
The shortened URL will be displayed below the input field.
Contributing
To contribute, fork the repository and create a feature branch off the master branch. Submit a pull request with your changes, and include clear descriptions of what you've added or modified.

## License
This project is licensed under the MIT License. Refer to the LICENSE file for details.


