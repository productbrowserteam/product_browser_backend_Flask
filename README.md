# product_browser_backend_Flask
backend made in Python with Flask framework


Current list of Endpoints:

https://product-browser1.herokuapp.com/category

GET - returns json with list of categories

POST - adds new category
json request format:
{"name" : name,   - required
"url": "url"         - required
"parentCategory: "parentCategory}

DELETE - deletes existing category

json request format:
{"name" : "name"}

https://product-browser1.herokuapp.com/category/modify

GET - used to fill base with categories from Cat.txt - do not user otherwise, will end up creating duplicates in db.

https://product-browser1.herokuapp.com/category/json

GET - returns formated categories json

POST - modify existing category
json request format:
{"newname" : "newname" -required
"name" : name,   - required
"url": "url"         - required
"parentCategory: "parentCategory}

https://product-browser1.herokuapp.com/product

GET - return list of products

POST - adds new product

request json format:
{ "name": "name",    - required
"url": "url",
"description": "description"
"subcategory": "subcategory"   -  required
"subcategoryUrl" : "subcategoryUrl"   -  required
"cid": "cid"}

DELETE - deletes existing product

json request format:
{"name" : "name"}

https://product-browser1.herokuapp.com/product/modify

POST - modify existing product:

products searched by name

json format:

{"name": "name"
"url": "url"
"description": "description"
"subcategory": "subcategory"
"subcategoryUrl": "subcategoryUrl"
"cid":: "cid"}
all required

https://product-browser1.herokuapp.com/product/json

GET - returns formated json for products
