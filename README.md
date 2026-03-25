# Hange Gallery
Hange Gallery is a Wagtail-based gallery site created to showcase my artwork of Hange Zoë from Attack on Titan, because I absolutely love Hange and wanted to build something fun while exploring Wagtail.

This project started as a small experiment but quickly became a great way to learn Wagtail features, reusable components, and custom UI styling.

## Features
- Artwork gallery organized into sections (like monthly collections)
- Individual artwork pages with high-quality images
- Reusable UI components
- Responsive images using Wagtail image tags
- Custom Bootstrap-based theme
- StreamField-powered flexible content

## Tech Stack
- Django
- Wagtail
- Bootstrap 5

## Project Structure
The project follows a modular Django app structure:

### Core Project
`hange_gallery/` — Main project configuration
  - `settings/` — Django settings configuration
  - `urls.py` — Root URL routing
  - `static/` — Project static files
  - `media/` — User-uploaded artwork

### Django Apps
`home`
- Defines the Home page
- Entry point of the gallery

`gallery`
- Core gallery functionality
- `GalleryPage` for sections
- `ArtworkPage` for individual artworks
- Suggested artwork block for ArtworkPages

`about`
- Artist profile
- Commission contact form

## Running Locally
```
git clone https://github.com/yourusername/hange-gallery
cd hange-gallery

python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt

python manage.py migrate
python manage.py loaddata initial_data.json   

python manage.py createsuperuser
python manage.py runserver
```

Then open:
`http://127.0.0.1:8000`

The initial_data.json file loads some sample pages and artwork so you can explore the gallery immediately.

## Screenshots

## Deployment
I'll deploy the project soon.

## Why I Built This
This project was mainly created to:
- Explore Wagtail features
- Experiment with building reusable components without a frontend framework

It also helped me understand how to structure a content-managed gallery site using Wagtail.
Plus it was just really fun to build.