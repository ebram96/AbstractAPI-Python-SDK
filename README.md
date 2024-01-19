# Abstract API Python SDK

This is a simple and intuitive Python SDK for using [AbstractAPI's](https://www.abstractapi.com/) services.

Current supported services:
===========================
All AbstractAPI services are supported by this SDK (16th. January 2023).
- Email Validation
- Phone Validation
- VAT Validation/Calculation/Categories
- IBAN Validation
- IP Geolocation
- Holidays Lookup
- Exchange Rates Live/Convert/Historical
- Company Enrichment
- Timezone Current/Conversion
- Avatars Generation
- Website Screenshot
- Website Scrape
- Image Processing

Installation:
=============
Install using `pip`:

    pip install abstract-api

Getting Started:
================
To use any service, you must have your API key for that service.\
To do that, you have two options:
1. Export your API key as an environment variable:\
   To export an API key for a service, you should follow this scheme:
   ```
   ABSTRACTAPI_{SERVICE_NAME}_API_KEY
   ```
   Note: `SERVICE_NAME` is all uppercase and underscore separated.\
   For example, to export your Email Validation service API key, use the following environment variable name:
   ```
   ABSTRACTAPI_EMAIL_VALIDATION_API_KEY
   ```
   Example in terminal:
   ```shell
   export ABSTRACTAPI_AVATARS_API_KEY=612345e4a63044b47a1234567a53cc81
   ```
   In initialization, you don't have to pass an API key:
   ```python
   from abstract_api import EmailValidation

   service = EmailValidation()
   ```
2. Pass your API key during service class instantiation:\
   Example:
   ```python
   from abstract_api import EmailValidation

   service = EmailValidation(api_key="612345e4a63044b47a1234567a53cc81")
   ```

**Note**:
If both options were used simultaneously, the API key that was passed to constructor is used.

Examples:
=========
**Notes**:
- Each service response is represented as a response class to provide an intuitive\
Pythonic way for handling responses.
- All public interfaces of all services classes are modeled after AbstractAPI endpoints interfaces and responses.\
  Example: Email Validation service endpoint expects the following parameters:
  - `api_key`
  - `email`
  - `auto_correct`\
  The `EmailValidation` class's `check()` method expects the same parameters `email` and `auto_correct`.\
  (No need to pass `api_key`. It is already passed during service instantiation.)

**Recommended**:\
- Check service class and service class response documentations.
- Response fields used in examples are not only the ones. Check documentation to see\
  all the capabilities.

- Email Validation
  ```
  >>> from abstract_api import EmailValidation
  >>> service = EmailValidation(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("example@example.com")
  >>> if response.is_valid_format:
  >>>    print("Email is valid!")
  >>> if response.is_disposable_email:
  >>>    print("Email is disposable, not this time :( ")
  ```
  `EmailValidation` documentation can be found [here](TODO)\
  `EmailValidationResponse` documentation can be found [here](TODO)

- Phone Validation
  ```
  >>> from abstract_api import PhoneValidation
  >>> service = PhoneValidation(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("20123456789")
  >>> if response.valid:
  >>>    print("Phone number is valid!")
  ```
  `PhoneValidation` documentation can be found [here](TODO)\
  `PhoneValidationResponse` documentation can be found [here](TODO)

- VAT Validation/Calculation/Inquiry
  ```
  >>> from abstract_api import VAT
  >>> service = VAT(api_key="612345e4a63044b47a1234567a53cc81")
  >>> validation_response = service.check("SE556656688001")
  >>> calculation_response = service.calculate(amount=100, country_code="EG")
  >>> categories_response = service.categories("EG")
  ```
  `VAT` documentation can be found [here](TODO)\
  `VATValidationResponse` documentation can be found [here](TODO)\
  `VATCalculationResponse` documentation can be found [here](TODO)\
  `VATCategoriesResponse` documentation can be found [here](TODO)

- IBAN Validation
  ```
  >>> from abstract_api import IBANValidation
  >>> service = IBANValidation(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("BE71096123456769")
  >>> if response.is_valid:
  >>>    print("IBAN is valid!")
  ```
  `IBANValidation` documentation can be found [here](TODO)\
  `IBANValidationResponse` documentation can be found [here](TODO)

- IP Geolocation
  ```
  >>> from abstract_api import IPGeolocation
  >>> service = IPGeolocation(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("156.215.70.7", fields=["city"])
  >>> print("IP is in: ", response.city)
  ```
  `IPGeolocation` documentation can be found [here](TODO)\
  `IPGeolocationResponse` documentation can be found [here](TODO)

- Holidays Lookup
  ```
  >>> from abstract_api import Holidays
  >>> service = Holidays(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("EG")
  >>> print(response.holidays)
  ```
  `Holidays` documentation can be found [here](TODO)\
  `HolidaysResponse` documentation can be found [here](TODO)

- Exchange Rates Live/Convert/Historical
  ```
  >>> from abstract_api import ExchangeRates
  >>> service = ExchangeRates(api_key="612345e4a63044b47a1234567a53cc81")
  >>> live_response = service.live("USD", "EGP")
  >>> conversion_response = service.convert("USD", "EGP", "2023-01-17", 150)
  >>> historical_response = service.historical("USD", "2023-01-17", 150)
  ```
  `ExchangeRates` documentation can be found [here](TODO)\
  `LiveExchangeRatesResponse` documentation can be found [here](TODO)\
  `HistoricalExchangeRatesResponse` documentation can be found [here](TODO)\
  `ExchangeRatesConversionResponse` documentation can be found [here](TODO)

- Company Enrichment
  ```
  >>> from abstract_api import CompanyEnrichment
  >>> service = CompanyEnrichment(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.check("EG")
  >>> print(response.holidays)
  ```
  `CompanyEnrichment` documentation can be found [here](TODO)\
  `CompanyEnrichmentResponse` documentation can be found [here](TODO)

- Timezone Current/Conversion
  ```
  >>> from abstract_api import Timezone
  >>> service = Timezone(api_key="612345e4a63044b47a1234567a53cc81")
  >>> current_response = service.current("Cairo, Egypt", "82.111.111.111")
  >>> conversion_response = service.convert((30.0594627, 31.1758899), "Cairo, Egypt")
  ```
  `Timezone` documentation can be found [here](TODO)\
  `CurrentTimezoneResponse` documentation can be found [here](TODO)\
  `TimezoneConversionResponse` documentation can be found [here](TODO)

- Avatars Generation
  ```
  >>> from abstract_api import Avatars
  >>> service = Avatars(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.create("John Doe", 200)
  >>> file = open("logo.png", "wb+")
  >>> file.write(response.content)
  ```
  `Avatars` documentation can be found [here](TODO)\
  `AvatarsResponse` documentation can be found [here](TODO)

- Website Screenshot
  ```
  >>> from abstract_api import WebsiteScreenshot
  >>> service = WebsiteScreenshot(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.capture("https://www.github.com", capture_full_page=False)
  >>> file = open("github-home-screenshot.png", "wb+")
  >>> file.write(response.content)
  ```
  `WebsiteScreenshot` documentation can be found [here](TODO)\
  `WebsiteScreenshotResponse` documentation can be found [here](TODO)

- Website Scrape
  ```
  >>> from abstract_api import WebScraping
  >>> service = WebScraping(api_key="612345e4a63044b47a1234567a53cc81")
  >>> response = service.scrape("https://www.github.com", proxy_country="EG")
  >>> file = open("github-home-screenshot.png", "wb+")
  >>> file.write(response.content)
  ```
  `WebScraping` documentation can be found [here](TODO)\
  `WebScrapingResponse` documentation can be found [here](TODO)

- Image Processing
  ```
  >>> from abstract_api import ImageProcessing
  >>> from abstract_api.image_processing.strategies import Crop, Exact
  >>> resize = Exact(height=200, width=200)
  >>> service = ImageProcessing(api_key="612345e4a63044b47a1234567a53cc81")
  >>> image = open('example.png', 'rb')
  >>> response = service.upload(image, lossy=False, resize=resize)
  >>> print(response.url)
  >>> response = service.url("https://example.com/image.jpeg", lossy=False, resize=resize)
  >>> print(response.url)
  ```
  `ImageProcessing` documentation can be found [here](TODO)\
  `ImageProcessingResponse` documentation can be found [here](TODO)

### Handling Errors
1. If something wrong happened on client side:
  ```
  >>> from abstract_api import ImageProcessing
  >>> from abstract_api.core.exceptions import ClientRequestError
  >>> service = ImageProcessing(api_key="612345e4a63044b47a1234567a53cc81")
  >>> try:
  >>>     service.url("https://example.com/image.jpeg", quality=150)
  >>> except ClientRequestError as e:
  >>>     print("Some error happended from client's side")
  >>>     print(str(e))
  >>> 'quality must be in range from 1 to 100 (inclusive)'
  ```
2. If the service endpoint returns a status code that is not 200 or 204.\
   (200 and 204 are -currently- the only accepted status codes.)
  ```
  >>> from abstract_api import ImageProcessing
  >>> from abstract_api.core.exceptions import APIRequestError
  >>> service = ImageProcessing(api_key="612345e4a63044b47a1234567a53cc81")
  >>> try:
  >>>     service.url("https://example.com/image.jpeg", quality=150)
  >>> except APIRequestError as e:
  >>>     if e.status_code == 500:
  >>>         print("AbstractAPI service is currently having a problem")
  >>>     print(str(e))
  ```
