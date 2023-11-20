from form_add import AddPropertyToForm
from zillow_scrape import ZillowScrape

zillow_scrape = ZillowScrape()
data = zillow_scrape.build_data()
add_to_form = AddPropertyToForm(data)

add_to_form.add_to_form()