from casdoor import CasdoorSDK

from settings import Settings

settings = Settings()


casdoor = CasdoorSDK(
    endpoint=settings.CASDOOR_ENDPOINT,
    client_id=settings.CASDOOR_CLIENT_ID,
    client_secret=settings.CASDOOR_CLIENT_SECRET,
    certificate=settings.CASDOOR_CERTIFICATE,
    org_name=settings.CASDOOR_ORG_NAME,
    application_name=settings.CASDOOR_APPLICATION_NAME,
)
