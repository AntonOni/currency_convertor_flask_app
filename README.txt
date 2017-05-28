=====================================
Discogs Takehome Assignment: Currency
=====================================

Thanks for applying at Discogs!

We want to assess your technical ability, but we also think coding under pressure in an interview is a terrible way to do that.

So as a compromise, here's a takehome exercise that's a simplified version of work you'd be doing at Discogs if you were hired.

Our goal is for this to take an hour (maybe two hours tops, if you're not very familiar with Python).
If it takes longer than that, we've failed, and you should let us know!

If we've made an error so grievous that you don't think you can finish the assignment, or you have any other questions after reviewing this document, feel free to email jhawkins@discogsinc.com and let Jason Hawkins know.


Description of the Problem
==========================
As we break the Discogs app up into smaller microservices, currency is one of our targets to break away from our main site.

Your assignment is to create a simple currency service that can provide conversion rates and convert currencies for consumers.

To keep this assignment short, you only need to support US Dollars, British Pounds Sterling, and Euros.
Wherever currencies appear in URL parameters or return data, you should specify them by their ISO 4217 codes (USD, GBP, EUR).

Please make use of a public currency conversion API for the actual rates.
(e.g., see https://duckduckgo.com/?q=currency+conversion+api)


Setup
=====

In this directory, we've included everything you should need to run a simple Flask-based API using Docker Compose.

In case you're not too familiar with Flask or Python, we've included a couple example API endpoints to illustrate how routing and responses work.

Assuming you have a working Docker installation locally, you should be able to just run:

docker-compose up

to start the app. It should be accessible on port 5000 of your docker machine's IP address.

For consuming the public currency conversion API, we've included the requests library, arguably Python's most popular and easiest-to-use HTTP client.


Goal
========
Please add the following endpoints to this API:

- GET /rate/currency1/to/currency2
    - Returns the conversion rate from currency1 to currency2 as a floating point number.
    - The rate should be the value of 1 unit of currency1 in currency2.
    - The return value should be a JSON object restating the request parameters and the rate.
    - Example request: http://example.tld:5000/rate/USD/GBP
    - Example response: JSON object like so:
        {
            'from': 'USD',
            'to': 'GBP',
            'rate':'0.768759'
        }

- GET /convert/currency1/amount/to/currency2
    - returns an amount in currency1 converted to currency2.
    - The return value should be a JSON object restating the request parameters and the converted amount.
    - All results should be rounded to 2 decimal points.
    - Example request: http://example.tld:5000/convert/USD/29.99/to/GBP
    - Example response: JSON object like so:
        {
            'from': 'USD',
            'from_amount': 29.99,
            'to': 'GBP',
            'converted_amount':'23.06'
        }


Finished?
==========
Congrats!

To get the code back to us, please either:
- zip it up and email it to jhawkins@discogsinc.com, or
- create a public Github repo for your finished code, and email the link to jhawkins@discogsinc.com

We're not going to hold you to a deadline, but if you can give us at least 24 hours before your interview, it'd be appreciated - we'll get to ask more interesting questions, too.

If you run out of time and have to bring a laptop to demo the code instead, no big deal!
You'll just need a way to plug an HDMI cable into your laptop to project your screen.

See you soon, and thank you!
Discogs Marketplace Squad
