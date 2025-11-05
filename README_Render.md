# Deploy Django app to Render

## One-time setup
1. Push this repo to GitHub.
2. Go to https://render.com, create a new Web Service and choose "Blueprint" → point to your GitHub repo with `render.yaml`.

## What this does
- Installs requirements
- Runs `collectstatic`
- Starts the app via Gunicorn

## Files added
- `Procfile` (runs Gunicorn)
- `runtime.txt` (Python version)
- `render.yaml` (Render blueprint)

## Notes
- Set `ALLOWED_HOSTS` in `relations_project/settings.py` to include your Render domain.
- Make sure `DATABASES` is configured. For SQLite, it works out of the box; for Postgres, add a Render Postgres and set `DATABASE_URL`.
