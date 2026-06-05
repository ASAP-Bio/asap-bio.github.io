# How to publish the ASAP-Bio website for free (GitHub Pages)

This folder is a complete, ready-to-publish website. You do **not** need any coding or the command line, everything below is done in your web browser by clicking and dragging.

Total time: about 15 minutes. Cost: free, forever.

---

## What you have in this folder

- `index.html` and six other pages (about, partners, themes, scholarships, news, contact)
- an `assets` folder (logos, stylesheet)
- a `.nojekyll` file (leave it; it tells GitHub to serve the files exactly as they are)

To preview it right now, just **double-click `index.html`**, it opens in your browser and every page works offline.

---

## Step 1, Create a free GitHub account
1. Go to **https://github.com** and click **Sign up**.
2. Use a project email if you can (e.g. a shared QGG/ASAP-Bio address) rather than a personal one, so the site is not tied to one person.

> **Recommended for a 5-year project:** after signing up, create a free **Organisation** (top-right **+** → *New organization* → Free plan) called something like `asap-bio`. Putting the website in an organisation means several colleagues can manage it and it survives staff changes. You can also do everything below in a personal account and move it later.

## Step 2, Create the repository (the place your files live)
1. Click the **+** (top right) → **New repository**.
2. **Repository name:**
   - For the cleanest address, create it inside an organisation named `asap-bio` and name the repository **`asap-bio.github.io`** → your site will be at **https://asap-bio.github.io**.
   - Otherwise name it **`asap-bio`** → your site will be at **https://YOUR-NAME.github.io/asap-bio/**. Both are free and fine.
3. Set it to **Public** (required for free Pages).
4. Leave everything else unticked and click **Create repository**.

## Step 3, Upload the website files
1. On the new repository page, click **Add file** → **Upload files** (or click the "uploading an existing file" link).
2. Open this `Website` folder on your computer, select **everything inside it**, the seven `.html` files, the `assets` folder, and the `.nojekyll` file, and **drag them onto the GitHub page**.
   - ⚠️ Upload the **contents** of the folder, not the folder itself. `index.html` must sit at the top level of the repository.
3. Scroll down and click **Commit changes**.

## Step 4, Turn on GitHub Pages
1. In the repository, click **Settings** (top menu) → **Pages** (left menu).
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Under **Branch**, choose **main** and folder **/ (root)**, then click **Save**.
4. Wait 1–2 minutes and refresh the page. GitHub shows a green box with your live link:
   - `https://asap-bio.github.io` (organisation repo), or
   - `https://YOUR-NAME.github.io/asap-bio/` (personal repo).

That link is your live website. Share it, and **put it in the first DANIDA annual report** (a web page link in Year 1 is a grant requirement).

---

## Updating the site later
Two easy ways, both in the browser:
- **Change wording on a page:** open the file in the repository, click the pencil ✏️ icon, edit, then **Commit changes**. The live site updates in ~1 minute.
- **Replace or add files (e.g. new news, new logo):** **Add file → Upload files**, drag the new/updated file, **Commit**.

To add a news item, edit `news.html` and copy one of the existing `<div class="item">…</div>` blocks.

---

## Optional, use your own domain (e.g. asap-bio.org)
1. Buy the domain from any registrar (≈ €10–15/year, this is the only thing that ever costs money, and it is optional).
2. In **Settings → Pages → Custom domain**, type your domain and **Save**.
3. At your registrar, add the DNS records GitHub shows you (a `CNAME` for `www`, or four `A` records for the root). GitHub gives free HTTPS automatically.

---

## Good to know
- **It's free and has no traffic limits** for a normal project site.
- **Nothing can "break" the server**, these are plain files; if an edit looks wrong, just re-upload the original from this folder.
- **The funding acknowledgement and the MFA + Danida Fellowship Centre logos** are already in the footer of every page, as the grant requires. Keep them there.
- **Keep the site live for at least 5 years after the project ends**, per the General Conditions.

---

### Need a hand?
The site is built as standard HTML/CSS, so any web-savvy colleague or your university web team can edit or extend it. The structure: each page is one `.html` file; shared styling lives in `assets/styles.css`.

---

## Troubleshooting: the page shows plain text, no styling, broken logo

This means the site loaded `index.html` but could **not** load `assets/styles.css` or the images, so the whole `assets/` folder is missing from the repository.

**Cause:** when uploading, the `assets` folder did not get included (dragging loose files does not create the subfolder).

**Fix (2 minutes):**
1. Open your repository on github.com.
2. Check the file list: you should see an `assets` folder next to `index.html`. If it is missing or empty, that is the problem.
3. Click **Add file -> Upload files**.
4. On your computer, open the `Website` folder, then **drag the `assets` folder itself** (not the files inside it) onto the GitHub page. Wait until you see paths like `assets/styles.css`, `assets/logo-au.png` listed.
5. Click **Commit changes**.
6. Wait 1-2 minutes, then **hard-refresh** the page (Ctrl+F5, or Cmd+Shift+R on Mac) to clear the cached unstyled version.

Tip: the easiest way to avoid this is to drag **all items** from the `Website` folder at once (every `.html` file **and** the `assets` folder together), and confirm `assets/` appears in the upload list before committing.
