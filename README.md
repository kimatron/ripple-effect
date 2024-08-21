# ripple-effect
A web application that raises awareness about marine conservation efforts and provides resources for individuals to get involved

# Ripple Effect

## Project Overview

Ripple Effect is a Django-based web application designed to raise awareness about marine conservation. The application provides information on marine protected areas, endangered species, and ongoing conservation initiatives.

## Features

- **Marine Protected Areas**: Display information about marine protected areas including their location, ecosystem type, and conservation status.
- **Endangered Species**: Show details about endangered species, their habitats, and conservation status.
- **Conservation Initiatives**: Highlight various conservation initiatives, including descriptions and links to their websites.

## Models

The application includes three main models:

### MarineProtectedArea

Represents a marine protected area with the following fields:
- `name`: The name of the protected area (CharField, max length 100).
- `location`: The location of the protected area (CharField, max length 200).
- `ecosystem_type`: The type of ecosystem found in the area (CharField, max length 100).
- `conservation_status`: The current conservation status of the area (CharField, max length 50).
- `description`: A detailed description of the area (TextField).
- `image`: An optional image of the area (ImageField, upload_to='protected_areas').

### EndangeredSpecies

Represents an endangered species with the following fields:
- `name`: The name of the species (CharField, max length 100).
- `species_type`: The type of species (CharField, max length 50).
- `conservation_status`: The conservation status of the species (CharField, max length 50).
- `habitat`: The natural habitat of the species (CharField, max length 200).
- `description`: A detailed description of the species (TextField).
- `image`: An optional image of the species (ImageField, upload_to='endangered_species').

### ConservationInitiative

Represents a conservation initiative with the following fields:
- `name`: The name of the initiative (CharField, max length 100).
- `organization`: The organization behind the initiative (CharField, max length 100).
- `description`: A detailed description of the initiative (TextField).
- `website`: The website URL of the initiative (URLField).
- `image`: An optional image related to the initiative (ImageField, upload_to='conservation_initiatives').

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kimatron/ripple-effect.git
   cd ripple-effect
   ```

   2 **Set up local environment**:
   ```bash
   python -m venv env
    source env/bin/activate  
    # On Windows, use `env\Scripts\activate` 
    ```
    3 **Install dependencies** :
    ```bash
    pip install -r requirements.txt
    ```
    4 **Apply migrations** :
    ```bash
    python manage.py migrate
    ```
     5 **Run in the development server** :
    ```bash
    python manage.py runserver
e
    ```
    Access the application at http://127.0.0.1:8000/.



## Usage
Marine Protected Areas: Navigate to the Marine Protected Areas section to view details about protected areas.
Endangered Species: Visit the Endangered Species section to learn about species at risk.
Conservation Initiatives: Check out the Conservation Initiatives section to find out about various conservation efforts.


## Contributing
Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.