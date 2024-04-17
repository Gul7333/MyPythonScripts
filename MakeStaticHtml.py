import sqlite3
import urllib.parse

# Connect to the SQLite database
conn = sqlite3.connect('./druginfostore.db')
cursor = conn.cursor()

# Retrieve data from the database
cursor.execute("SELECT * from medinfo_drugs")
pages = cursor.fetchall()
print(len(pages))
print(pages[0][3])
for item in pages:
    drugname, overview, indication , sideeffect, contra, warn, highrisk = item
    print('drug name => ', drugname)
    html_content = f"""
<!doctype html>
<html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="theme-color" content="#E0F7FA" />
      <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css">
      <link rel="manifest" href="/manifest.json"  />
     
     <meta name="description" content="latest price of {drugname}">
     <meta name="description" content="{drugname} : {indication}, {sideeffect}">
       <meta name="description" content="{contra}, {warn}, {highrisk}">
<meta property="og:{drugname} indication, and latest price" content="{overview},{indication}">
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="Style.css" type="text/css" media="all" />
        <title>{drugname} indication and latest price </title>

<script src="./sql-wasm.js"></script>
   <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3179201948946967"
     crossorigin="anonymous"></script>
    </head>
    <body>
    
        <div class="loader">
            <span class="loaderr"></span>
        </div>
        <div class="top">
            <center data-logo>
                <img width="230" src="./logo.png" alt="" />
            </center>
        </div>
        <article class="main">
            <input
                type="search"
                class="search"
                id="search"
                value="headache"
                placeholder="Search Any disease"
            />
            <button class="searchBtn">Search</button>
       <div data-suggestion data-suggestion-hide>
       </div>
        </article>
          <a data-top-buttons href="/Favorite.html">Favourite Drugs</a>
        <article class="results">
            
             <div class="drug">
            <h4>{drugname}</h4>
            <button onclick=showBrands(event)  class="brand">Brands</button>
            <button onclick=addFav(event) class="fav"><img width='120%' src='./heart.png'></img></button>
            <b> {drugname} Over View</b>
            <p class="drug_overview">{overview}</p>
            <b> {drugname} Indications</b>
            <p class="drug_indications">{indication}</p>
            <b>{drugname} Side Effects</b>
            <p class="drug_side_effect">{sideeffect}</p>
          </div>
        </article>

      <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/toastify-js"></script>
      <script src="Script.js" type="module" charset="utf-8" ></script>
    </body>
</html>

    """
    drugname = drugname.replace('/', '-')
        
    with open(f'pages/{drugname}.html','w') as file:
        file.write(html_content)

conn.close()


# Iterate over the pages and generate HTML content
# for page in pages:
#     page_id, title, content = page
#     html_content = f"""
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>{title}</title>
#         </head>
#         <body>
#             <h1>{title}</h1>
#             <div>{content}</div>
#         </body>
#         </html>
#     """
#
#     # Write HTML content to a file
#     with open(f'pages/page_{page_id}.html', 'w') as file:
#         file.write(html_content)
#
# Close the database connection
conn.close()

