Feature: Create skill user pair and test if returned user_name matches the created

    Background:
    * url base_url
    * def request_random =
            """
            function(addRandomTo){
            var longRandom=java.util.UUID.randomUUID().toString();
            longRandom=longRandom.replace('-','');
            longRandom=longRandom.substring(0,5);
            return addRandomTo + longRandom;
            }
            """
    * def request_create = read('classpath:requests/createUserSkill.json')
    * set request_create.user_name = call request_random 'abc'
    * set request_create.skill_name = 'dbc'

    @smoke
    Scenario: Call post to create random user skill combo
        Given path 'api','v1','skills','create'
        And request request_create
        When method post
        Then status 201
        And match response.user_name == request_create.user_name



