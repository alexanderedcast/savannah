
class JourneyLocator(object):

    section_title = "//div[@class='pathway-content']//div[contains(@class, 'journey-section-header')]/input"
    journey_tag_input = "(//div[@class='row']//div[@class='text-block']//input[@type='text'])[3]"
    weekly = "(//div[@class='input-block']//div[@class='small-12 medium-8 large-9']//div[@style='display: flex;']//input[@value='weekly']/..//div[@style]/div/*[@viewBox])[1]"
    self_paced = "(//input[@value='self_paced']/..//div[@style]/div/*[@viewBox])[2]"
    channel_button = "//div[@class='input-block']//div[@class='text-block']//div[contains(@id, 'Channel')]//button"
    channel = "//div[@data-reactroot]//div//span[contains(@class, 'postToChannel')]//div[text()='%s']"
    date_input = "//div[@class='common-block']//div[@class='small-12 medium-8']//div[@class='row']//div//input[contains(@id, 'SelectaDate')]"
    remove_section = "//div[@class='journey-part__container']//button[contains(@class, 'title')]//span[text()='REMOVE']"
    add_section_button = "//button[@type='button']//span[text()='+ Add']"
