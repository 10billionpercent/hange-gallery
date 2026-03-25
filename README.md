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
<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/7ba53943-fcdc-4117-ae1e-cf156b9af32d" />

### Gallery Page
<img width="1919" height="859" alt="image" src="https://github.com/user-attachments/assets/1d9f491b-81b9-4650-964a-c23734d6da80" />

### Artwork Page
<img width="1919" height="858" alt="image" src="https://github.com/user-attachments/assets/0abc32f0-2ee3-41c9-ae52-44c657375d45" />

### About Page
<img width="1919" height="863" alt="image" src="https://github.com/user-attachments/assets/c0d7041f-bc85-439f-9af8-3c9381d0daa1" />

### Commission modal
<img width="1919" height="854" alt="image" src="https://github.com/user-attachments/assets/785545c2-93df-404e-ac7c-7212cbd94dff" />

### Commission form success state
<img width="1919" height="866" alt="image" src="https://github.com/user-attachments/assets/8a65119d-ecc3-4fe7-954d-12d63b261738" />

### Commission form error state
<img width="1919" height="851" alt="image" src="https://github.com/user-attachments/assets/6adf228c-580e-4d25-850b-afea9fe60846" />

## Deployment
I'll deploy the project soon.

## Why I Built This
I had been meaning to build a small website for my artwork for a while, and this felt like the perfect chance to do it while exploring Wagtail.

So this project became both
- a small personal gallery
- and a fun way to experiment with Wagtail features and reusable components.
