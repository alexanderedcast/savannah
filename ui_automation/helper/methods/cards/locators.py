# coding=utf-8
class SmartCardLocators(object):
    link_input = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[1]"
    description_input = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[2]"
    button_create_smartcard = "//div[@class='action-buttons']//button[@class='create']"
    preview_upload = "(//div[contains(@class, 'preview')])[last()]"
    upload_menu = "//div[@class='fsp-modal']"
    input_my_device_upload = "//div[@class='fsp-drop-area']//input"
    type_of_smartcard = "(//div[@class]//div[contains(@class, 'small-3 type-block')]/div//div[@class]/span[text()='%s']/../../div)[1]"
    upload_content = "//div[@class='fsp-footer__nav']//span[@class]/div/span[@title='Upload']"
    text_input_area = "//div[@class]//div[@class='inputs-block']//div[contains(@class, 'public-DraftEditor-content')]"
    first_choice_field = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[2]"
    second_choice_field = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[3]"
    third_choice_field = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[4]"
    text_card_details = "(//div[contains(@class,'marked-text ')]/p)[1]"
    to_inside_card = "(//div[@data-reactroot]//div[contains(@class, 'card')]//div[contains(@class, 'card')]//div[contains(@class, 'card')]//div[contains(@class, 'details')])[1]"
    resource_inside_link_card = "//div[@class='resource']"
    image_container = "//div[@class='image-container']"
    poll_title_inside_card = "//div[@class='insight-container']//div[@class='message']//div[@class]/p"
    num_of_choices_inside_card = "(//div[@data-reactroot]//div[@class='stand-alone']//div[@class='vertical-spacing-medium']//input)[1]"
    poll_option_radio_button = "(//input[@type='radio'])[%s]"
    poll_radio = "//input[@type='radio']"
    vote_poll_card = "//button[@class='vote']"
    change_image = "//div[@data-reactroot]//div[@class='smartbite-creation']//div[@class='card-img-container']/div"
    add_choice = "//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//div[@class='text-block']/span/span"
    quantity_of_poll_option = "(//div[@class='vertical-spacing-medium'])[2]/div/input"
    complexity_level = "//div[@style='display: flex;']/div[@class]/input[@name='bia-radio']"

    #################
    # Quiz card
    #################
    first_field = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[3]"
    second_field = "(//div[@class]//div[contains(@class, 'smart')]//div[@class='inputs-block']//input)[5]"
    correct_answer = "(//div[@class='quiz-item']//input[@type='checkbox'])[1]"
    inside_container = "//div[@class='insight-container']"

    #################
    # Dynamic Pathway
    #################
    enter_topic = "//div[@data-reactroot]//div[@class='additional-block']//input[@type='text']"
    number_dynamic_card = "//div[@data-reactroot]//div[@class='additional-block']//select/option[@value][text()='%d']"

    #################
    # From Bookmark
    #################
    topic_for_bookmark_card = "(//div[@class='cards-search-list']//span//div[@style]//div[@class='search-block'])[1]"

    #################
    # Poll Card
    #################
    content_upload_player = "//div[@class='text-center relative']//div[@class='preview-video']"
    upload_picture = "//button[@class='imageUpload']"
    video_inside_card = "//div[@class='resource']//div[@class='inline-video']"
    vertical_spacing = "//div[@class='vertical-spacing-medium']/div[@class='vertical-spacing-medium']"


    #################
    # Advanced Setting
    #################
    dropdown_menu = "//select[@class='journey-weeks-dropdown']"
    advanced_setting = "//div[@class='advanced-settings']//div[@class='advanced-label']/span"
    provider_name = "//div[@class='advanced-settings']//div[@class='smartbite-input']//input[contains(@id, 'EnterProviderName')]"
    card_type = "(//select[@class='journey-weeks-dropdown']/option/span)[%s]"
    all_options = "//select[@class='journey-weeks-dropdown']/option/span"

    card_type_inside_card = "//span[@class='card-type']//span"
