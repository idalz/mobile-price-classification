index_dict = {
    "title": "Home",
    "quote_h2": "Choose your <span>Spects</span><br> Get our <span>Estimates</span>",
    "quote_p": "Effortlessly and accurately gauge the worth of mobile devices by selecting specifications and receiving instant valuations.",
    "quote_button": "Make a Prediction"
}

form_dict = {
    "title": "Mobile Information Form",
    "form_title": "Mobile Information Form",
    "form_button": "Predict Price"
}

about_dict = {
    "title": "About this Project",
    ### About the project
    "project_title": "About the Project",
    "project_descr": """
    With the ever-growing variety of mobile devices available in the market, accurately determining their class based on specifications is a challenging task.
    Many factors such as battery power, RAM capacity, camera resolution, and connectivity options contribute to the classification process.
    Our mission is to address this complexity and develop a solution that reliably categorizes mobile devices into their appropriate classes.<br><br>

    <strong>Our primary goal</strong> is to leverage machine learning techniques to <strong>build a highly accurate classification model</strong> for mobile devices.
    By analyzing extensive datasets containing mobile specifications and their corresponding classes, we aim to develop a model capable of precisely identifying
      the class of a mobile device based on its features.
    """,
    ### About the model
    "model_title": "About the Model",
    "model_descr": """
    The model is a <strong>simple Linear Regression model</strong> trained on a comprehensive dataset from Kaggle.
     During training, the features were preprocessed and scaled for optimal performance. 
     It is able to calculate the class of a mobile based on its features 
     with a high <strong>micro F1-score of 0.98</strong>.

    """,
    ### About the data
    "data_title": "About the Data",
    "data_descr": """
    The dataset obtained from Kaggle's <a href="https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification" style="color: var(--primary-color-1)";>
    Mobile Price Classification</a> consists of mobile specifications and their corresponding price classifications.<br>

    <br><strong>battery_power</strong>: The battery power of the mobile device (measured in mAh)
    <br><strong>blue</strong>: Indicates Bluetooth support (1 for Yes, 0 for No)
    <br><strong>clock_speed</strong>: The clock speed of the device's CPU (measured in GHz)
    <br><strong>dual_sim</strong>: Indicates Dual SIM support (1 for Yes, 0 for No)
    <br><strong>fc</strong>: The resolution of the front camera (in megapixels)
    <br><strong>four_g</strong>: Indicates 4G support (1 for Yes, 0 for No)
    <br><strong>int_memory</strong>: The internal memory capacity of the device (in GB)
    <br><strong>m_dep</strong>: The mobile depth (measured in cm)
    <br><strong>mobile_wt</strong>: The weight of the mobile device (measured in grams)
    <br><strong>n_cores</strong>: The number of CPU cores
    <br><strong>pc</strong>: The resolution of the primary camera (in megapixels)
    <br><strong>px_height</strong>: The pixel height of the device's display
    <br><strong>px_width</strong>: The pixel width of the device's display
    <br><strong>ram</strong>: The RAM capacity of the device (measured in megabytes)
    <br><strong>sc_h</strong>: The screen height of the device (measured in cm)
    <br><strong>sc_w</strong>: The screen width of the device (measured in cm)
    <br><strong>talk_time</strong>: The talk time of the device (measured in hours)
    <br><strong>three_g</strong>: Indicates 3G support (1 for Yes, 0 for No)
    <br><strong>touch_screen</strong>: Indicates Touch Screen presence (1 for Yes, 0 for No)
    <br><strong>wifi</strong>: Indicates Wi-Fi support (1 for Yes, 0 for No)
    <br><strong>price_range</strong>: The price range of the mobile device (categorized)
    """,
}