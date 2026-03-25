# Hange Gallery
Hange Gallery is a Wagtail-based gallery site created to showcase my artwork of Hange Zoë from Attack on Titan, because I absolutely love Hange and wanted to build something fun while exploring Wagtail.

This project started as a small experiment but quickly became a great way to explore Wagtail features, reusable components, and custom UI styling.

## Features
- Artwork gallery organized into sections (like monthly collections)
- Individual artwork pages with high-quality images
- Reusable UI components
- Responsive images using Wagtail image tags
- Custom Bootstrap-based theme
- StreamField-powered flexible content

## Tech Stack
- Wagtail
- Bootstrap 5

## Project Structure
The project follows a modular Django app structure -

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

Then open
`http://127.0.0.1:8000`

The `initial_data.json` file loads some sample pages and artwork so you can explore the gallery immediately.

## Screenshots
### Home Page


### Gallery Page


### Artwork Page


### About Page


### Commission modal



## Deployment
I'll deploy the project soon.

## Why I Built This
I had been meaning to build a small website for my artwork for a while, and this felt like the perfect chance to do it while exploring Wagtail.

So this project became both
- a small personal gallery
- and a fun way to experiment with Wagtail features and reusable components.