# 2D Blueprint to 3D Model

Welcome to the **2D Blueprint to 3D Model** project! This repository provides a solution for converting 2D architectural blueprints into 3D models using a combination of machine learning and computer vision techniques.

![Blueprint to 3D](https://img.shields.io/badge/Blueprint_to_3D_Model-Active-brightgreen) ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-blue) ![License](https://img.shields.io/badge/license-MIT-orange)

## 🚀 Project Overview

This project aims to automate the transformation of 2D floor plans into 3D models, saving time and enhancing accuracy for architects, designers, and construction professionals. The system leverages deep learning models to detect key elements in a blueprint and generate a corresponding 3D representation.

---

## ✨ Features

- **2D to 3D Conversion**: Automatically generate 3D models from 2D blueprints.
- **Room Detection**: Accurately detect and label rooms based on architectural designs.
- **Structure Recognition**: Identify doors, windows, walls, and other key structures in a 2D blueprint.
- **Modular Design**: Easily extensible to support additional features and improve accuracy.
- **Visualization**: View the generated 3D models interactively.

---

## 🛠️ Setup Guide

Follow these steps to get the project up and running on your local machine:

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- pip (Python package manager)
- Git

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/jayant1554/2d_blueprint_to_3d_model.git
   cd 2d_blueprint_to_3d_model

Create a Virtual Environment:

It's recommended to use a virtual environment to manage dependencies.

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Install the required Python packages using the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Run the Application:

After installation, you can start the application using:

bash
Copy code
python main.py
This will launch the backend server for processing the 2D blueprint images and generating the 3D model.

Access the Frontend:

Once the backend is running, you can access the web-based frontend for interacting with the application. Open your web browser and navigate to:

bash
Copy code
http://localhost:5000
Here, you will be able to upload a 2D blueprint image and view the generated 3D model interactively.

🔥 Deployment
You can deploy this application using Docker or cloud platforms such as Heroku or AWS.

Deploy with Docker
Create a Dockerfile:

Inside the root of your project directory, create a Dockerfile:

dockerfile
Copy code
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_ENV=production

# Run the application
CMD ["python", "main.py"]
Build the Docker Image:

Run the following command to build the Docker image:

bash
Copy code
docker build -t blueprint-to-3d .
Run the Docker Container:

Once the image is built, run it with:

bash
Copy code
docker run -p 5000:5000 blueprint-to-3d
The application will be accessible at http://localhost:5000.

Deploy on Heroku
Install Heroku CLI if you don’t have it installed. Download it here.

Login to Heroku:

bash
Copy code
heroku login
Create a Heroku app:

bash
Copy code
heroku create your-app-name
Add a Procfile in the root directory to specify the application entry point:

text
Copy code
web: python main.py
Push the code to Heroku:

bash
Copy code
git push heroku main
Scale the web process:

bash
Copy code
heroku ps:scale web=1
Open the app:

bash
Copy code
heroku open
Deploy on AWS Elastic Beanstalk
Install the AWS CLI and configure it with your credentials. Follow the instructions here.

Initialize Elastic Beanstalk:

bash
Copy code
eb init
Follow the prompts to configure your application.

Create an Environment and Deploy:

bash
Copy code
eb create
eb deploy
Open the Application:

bash
Copy code
eb open
📂 Project Structure
bash
Copy code
2d_blueprint_to_3d_model/
│
├── backend/            # Contains all backend logic
├── frontend/           # Contains the user interface (UI) code
├── blueprints/         # Sample blueprints for testing
├── models/             # Pretrained and custom models for blueprint analysis
├── README.md           # Project documentation (this file)
├── requirements.txt    # Python dependencies
├── main.py             # Main entry point to run the application
└── utils.py            # Utility functions
🤝 Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature-name).
Open a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
