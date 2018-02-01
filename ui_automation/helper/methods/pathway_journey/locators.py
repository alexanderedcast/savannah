class PackLocators(object):
    ############################
    # Journey and Pathway
    ############################
    title = "(//div[@class='row']//div[@class='text-block']//input)[1]"
    description = "(//div[@class='row']//div[@class='text-block']//input)[2]"
    add_smartcard = "//div[@class='empty-smartbite']//div[@class='text-center']"
    ##############
    # Channels
    ##############
    channel = "//div[@class='row']//div[contains(@id, 'Channel')]"
    menu_channel = "(//div[@data-reactroot]//div[@style]/div/span[contains(@class, 'postToChannel')])[1]"
    choose_channel = "//div[@data-reactroot]//div[@style]/div/span[contains(@class, 'postToChannel')]//div[@style]//div[text()='%s']"
    delete_channel = "(//div[@class='chip-channel-pathway-item']/div//*[@viewBox])[1]"
    channel_name = "(//div[@class='chip-channel-pathway-item']/div/span)[1]"
    done_card = "(//div[@data-reactroot]//div[@class='additional-block']//button[@class])[last()]"
    publish = "//div[@data-reactroot]//div[contains(@class,'pathway-creation')]//div[@class='action-buttons']//button[@class='publish']"
    ok_pathway = "//div[@class]/div//div[@class='StatusModal']//button[@class='confirmStatus']"
    add_card_type = "//div[@class='row']//div[@class='small-3 card-circle']//div[@class]/span[text()='%s']/../../div[@class]"
    menu_pathway = "//div[@class]//div[@class='paper-card']//div[@class]//span[text()='PATHWAY']/../../../..//div[@class='actions-bar']//div[@class='insight-dropdown']/button"
    delete_second_card_from_pathway = "(//div[@class='smartbites-block']//div[@id='listWithHandle']/div[@class]//div[@class='close close-button pathway-card-btn close-card-btn'])[2]"
    delete_first_card_from_pathway = "(//div[@class='smartbites-block']//div[@id='listWithHandle']/div[@class]//div[@class='close close-button pathway-card-btn close-card-btn'])[1]"
    cards_inside_pathway = "//div[@class='smartbites-block']//div[contains(@class, 'card-v')]"
    label = "//div[@class='pathway-label-block']/div[@class]//span[text()]"
    preview_upload = "//div[@class='preview-upload']//div[@class='card-img-container']//div[@class='card-img button-icon']"
    description_inside_card = "//div[@id='description']/span"
    card_banner = "//div[@class='pathway-banner']/div[@class]"
    banner_preview = "//div[@class='pathway-banner preview-upload']/div[@class]"
    save_for_later = "//div[@class='action-buttons']//button[@class='saveLater']"
    draft_label = "(//div[@class='paper-card']//div[@class='pathway-label-block']//span[text()='DRAFT'])[1]"
    card_overview_content = "//div[@class='modalContainer modal']//div[@class='card-overview']"
    image_link = "//div[@class='verify_number_skills-image card-image-block']"
    card_logo = "//div[@class='smartbite-overview']//div[@class='logo-type']//span[@class='label-text'][text()='%s']"
    card_image_block = "//div[@class='verify_number_skills-image card-image-block']//div[@class='card-blurred-background']"
    close_button_inside_pathway = "//div[@class='close close-button']//button"

    poll_option = "//div[@class='modalContainer modal']//div[@class='vertical-spacing-medium']//input"
    radio_button = "(//div[@class='modalContainer modal']//div[@style]//div[@style]//input[@type='radio'])[%s]"




