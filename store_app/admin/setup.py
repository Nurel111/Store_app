from .views import (UserProfileAdmin, CategoryAdmin, ProductAdmin,
                    ProductImageAdmin, RefreshTokenAdmin, ReviewAdmin, SubCategoryAdmin)
from fastapi import FastAPI
from sqladmin import Admin
from store_app.database.db import engine

def setup_admin(store_app: FastAPI):
    admin = Admin(store_app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(ProductImageAdmin)
    admin.add_view(RefreshTokenAdmin)
    admin.add_view(ReviewAdmin)
    admin.add_view(SubCategoryAdmin)