from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from users.views import RegisterView, LoginView
from cources.views import CourseViewSet
from enrollments.views import EnrollmentViewSet
from quizzes.views import QuizViewSet, QuizResultViewSet
from assignments.views import AssignmentViewSet, SubmissionViewSet
from payments.views import PaymentViewSet
from django.conf import settings
from django.conf.urls.static import static

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public=public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="ONLINE LEARNING API",
        default_version="v1",
        description="Online Learning web application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="olacodeire@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[permissions.AllowAny],
)

# Initialize the router and register the viewsets
router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'quiz-result', QuizResultViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submission', SubmissionViewSet)
router.register(r'payments', PaymentViewSet)

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="swagger-redoc"),
    path('api/', include(router.urls)),
]



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )