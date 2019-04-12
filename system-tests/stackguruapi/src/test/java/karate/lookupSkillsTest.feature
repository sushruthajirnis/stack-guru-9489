Feature: Look up all existing skills and users

    Background:
    * url base_url
    * configure headers = read('classpath:headers.js')
    @smoke
    Scenario: Get call to show all skills of users
        Given path 'api','v1','skills'
        When method get
        Then status 200
        And assert response.length > 0
        