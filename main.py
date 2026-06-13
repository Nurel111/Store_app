from fastapi import FastAPI
import uvicorn
from store_app.admin.setup import setup_admin
from store_app.api import users,category,subcategory,product,product_image,auth


shop_app = FastAPI(title="Shop_app")
shop_app.include_router(users.users_router)
shop_app.include_router(category.category_router)
shop_app.include_router(product.product_router)
shop_app.include_router(product_image.product_image_router)
shop_app.include_router(subcategory.subcategory_router)
setup_admin(shop_app)

if __name__ == '__main__':
    uvicorn.run(shop_app, host="127.0.0.1", port=8000)