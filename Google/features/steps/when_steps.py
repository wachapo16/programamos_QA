from behave import when


@when('I search for "{keyword}"')
def step_search_for_facebook(context, keyword):
    context.home_page.search_for(keyword)
