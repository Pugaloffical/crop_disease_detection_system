# TODO
- [x] Update `detector/templates/detector/login.html` to render username/password fields explicitly and display Django auth errors.
- [x] Update `detector/static/css/style.css` with styles for error lists/field errors used by Django.
- [x] Run the Django server and verify `/accounts/login/` shows styled fields and errors when login fails.
- [x] Create new frontend page at `/frontend/` by adding:
  - [x] New view `views.frontend` (reuse scanner logic)
  - [x] New template `detector/templates/detector/frontend.html` (copy UI from `scanner.html`)
  - [x] New URL route `/frontend/` in `detector/urls.py`
  - [x] Add nav link in `detector/templates/detector/base.html`
- [ ] Run server and test `/frontend/` loads form and redirects to result after upload.
- [x] Fix login/register redirect destination ("main page") after auth.
- [x] Fix dashboard template variable `top_disease` (missing in `views.dashboard`).

