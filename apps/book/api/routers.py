from rest_framework import routers
from rest_framework.routers import DefaultRouter
from apps.book.api.viewsets.book_viewsets import BookModelViewSet
from apps.book.api.viewsets.author_viewsets import AuthorModelViewSet
from apps.book.api.viewsets.category_viewsets import CategoryModelViewSet
from apps.book.api.viewsets.partner_viewsets import PartnerModelViewSet
from apps.book.api.viewsets.book_loan_viewsets import BookLoanModelViewSet

router = DefaultRouter()
router.register(r'book', BookModelViewSet, basename='books')
router.register(r'author', AuthorModelViewSet, basename='author')
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'partner', PartnerModelViewSet, basename='partner')
router.register(r'bookloan', BookLoanModelViewSet, basename='bookloan')

# exportamos las rutas al apiRoot
urlpatterns = router.urls