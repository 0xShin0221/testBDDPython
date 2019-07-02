Feature: Friendships

	Background: Set up common data

		Given I empty the "User" table

		And I create the following users:
		  | id | email             | username | password  |
		  | 1  | annie@example.com | Annie    | pAssw0rd! |
		  | 2  | brian@example.com | Brian    | pAssw0rd! |
		  | 3  | casey@example.com | Casey    | pAssw0rd! |

		When I log in with username "Annie" and password "pAssw0rd!"

		Then I am logged in

	Scenario: A user can see a list of friends

		Given I empty the "Friendship" table

		And I create the following friendships:
		  | id | user1 | user2 |
		  | 1  | 1     | 2     |

		# Annie and Brian are now friends.

		When I get a list of friends

		Then I see the following response data:
		  | id | email             | username |
		  | 2  | brian@example.com | Brian    |

	Scenario: A user with no friends sees an empty list

		Given I empty the "Friendship" table

		# Annie has no friends.

		When I get a list of friends

		Then I see the following response data:
		| id | email | username |