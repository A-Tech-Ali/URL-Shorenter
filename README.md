# URL Shortener

A simple URL shortener application built with Python and Flask, using `shortuuid` to generate short, human-readable URLs.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

This URL shortener is a web application that allows you to create shortened versions of long URLs, making them more manageable and user-friendly. It uses the `shortuuid` library to generate short, unique identifiers for the URLs.

## Features

- Shorten long URLs into compact, user-friendly links.
- Redirect users to the original long URL when they access the shortened link.
- Generate unique short URLs using `shortuuid`.

## Getting Started

### Prerequisites

Before you can run this application, you need to have the following installed:

- Python 3.x
- Flask (`pip install Flask`)
- `shortuuid` (`pip install shortuuid`)

### Installation

1. download the zip
2. Run the Flask application:
   ```bash
   python main.py
### Usage

1. Access the URL shortener web interface at http://127.0.0.1:5000/.
2. Enter a long URL that you want to shorten and click the "Shorten URL" button.
3. The application will generate a shortened URL, which you can use to access the original long URL.
