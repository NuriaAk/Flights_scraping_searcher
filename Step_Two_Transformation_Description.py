if __name__ == '__main__':

    import logging
    logging.basicConfig(filename='step_two_logfile.log', filemode='w', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO)

    # Open a file
    from Classes import Class_FileManager
    data_file = Class_FileManager.FileManager(name_of_file_with_data='flight_prices_september.csv')
    df = data_file.open_data()
    logging.info('%s Initial csv is opened')

    # Transform Data
    from Classes import Class_DataTransformer
    data_transform = Class_DataTransformer.DataTransformer()

    # Create a new df without blank variables
    clean_df = data_transform.no_blank_values_df(df)
    # Transform the price value into INT
    clean_df['price'] = data_transform.transf_price_into_int(df['price'])
    # Save the cleaned file to the folder
    clean_data_file = Class_FileManager.FileManager()
    clean_data_file.save_clean_data(clean_df)

    # Let's explore the prices
    from Classes import Class_DataDescriptor
    data_description = Class_DataDescriptor.DataDescriptor(clean_df)

    data_description.top_cheapest_airlines()
    logging.info('%s Cheapest Airlines are shown')

    data_description.average_price_number_stop()
    logging.info('%s Average prices per numbers of stops are shown')

    data_description.average_price_am_pm()
    logging.info('%s Average prices per departure time are shown')
