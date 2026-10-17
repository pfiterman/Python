# Fixtures
# Fixtures are a type of function that is applied to functions to be tested. 
# These functions must run before that test is executed. The purpose of fixtures is to supply data from multiple sources including URLs and databases 
# to the test before running the test. Fixtures are used in cases where code repeats initialization.

# Format:  @pytest.fixture

# Markers
# Markers are used to 'mark' specific functions to be executed by letting users create special names. 
# There are many built-in markers such as xfail, xpass, skip and so on.

# They follow a format such as:  @pytest.mark.<markername> 

# For example:
# @pytest.mark.alpha 
# Running the specific marked test in the command line can be done with the following command:

# pytest -m <markername> -v 
# Which will be as follows for a marker called alpha.
# pytest -m alpha -v 