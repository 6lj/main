#!/usr/bin/env python3

import os

print("Content-Type: text/html")  # Specify HTML content
print()  # Blank line to end headers

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CGI Example</title>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            height: 100vh;
            background-color: #f4f4f9;
            overflow: hidden;
            text-align: center;
        }
        .social-links {
            margin-top: 20px;
            display: flex;
            gap: 12px;
            justify-content: center;
        }
        .social-link {
            text-decoration: none;
            font-weight: 500;
            padding: 10px 28px;
            border-radius: 25px;
            transition: all 0.3s ease;
            color: white;
        }
        .gameguardian { background-color: #800080; }
        .iosgods { background-color: #007aff; }
        .github { background-color: #333; }
        .cv { background-color: #4caf50; }
    </style>
</head>
<body>
    <div>
        <h1>Welcome to My CGI Page</h1>
        <div class="social-links">
            <a href="https://gameguardian.net" target="_blank" class="social-link gameguardian">Game Guardian</a>
            <a href="https://iosgods.com" target="_blank" class="social-link iosgods">iOSGods</a>
            <a href="https://github.com" target="_blank" class="social-link github">GitHub</a>
            <a href="cv.pdf" target="_blank" class="social-link cv">CV</a>
        </div>
    </div>
</body>
</html>
"""

print(html_content)
