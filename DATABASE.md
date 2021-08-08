
# Database Schema:

The database "Creative Cooking" will contain 4 collections: Users, Recipes, Cuisine and Categories


## Users collection:

Schema

  {

    "_id"      :    <ObjectID>
    "username" :    <string>
    "password" :    <string>

  }

Example

  {

    "_id"      :    <ObjectID>
    "username" :    "admin"
    "password" :    "admin"

  }


## Recipes collection:

Schema

  {

    "_id"               :    <ObjectID>
    "dish_name"         :    <string>
    "category_name"     :    <string>
    "cuisine_name"      :    <string>
    "preparation_steps" :    <string>
    "image_url"         :    <string>
    "tools"             :    <string>
    "created_by"        :    <string>
    "ingredients"       :    <string>
    "img_description"   :    <string>

  }

Example

  {

    "_id"               :    <ObjectID>
    "dish_name"         :    "Quality Street"
    "category_name"     :    "Sweets"
    "cuisine_name"      :    "International"
    "preparation_steps" :    "no steps, ready to eat"
    "image_url"         :    "https://i.ibb.co/G7fnNsV/project-3-img-dish-001.jpg"
    "tools"             :    "hands"
    "created_by"        :    "admin"
    "ingredients"       :    "Milk, chocolate, sugar"
    "img_description"   :    "Quality Street"

  }

## Cuisine collection:

Schema

  {

    "_id"           :    <ObjectID>
    "cuisine_name"  :    <string>

  }

Example

  {

    "_id"           :    <ObjectID>
    "cuisine_name"  :    "International"

  }

## Categories collection:

Schema

  {

    "_id"           :    <ObjectID>
    "category_name" :    <string>

  }

Example

  {

    "_id"           :    <ObjectID>
    "category_name" :    "Sweets"

  }