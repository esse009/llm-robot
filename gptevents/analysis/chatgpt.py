# by Pavlo Bazilinskyy <pavlo.bazilinskyy@gmail.com>
import os
import pandas as pd
from tqdm import tqdm


import gptevents as gpte

# warning about partial assignment
pd.options.mode.chained_assignment = None  # default='warn'

logger = gpte.CustomLogger(__name__)  # use custom logger


class ChatGPT:
    # pandas dataframe with extracted data
    data = pd.DataFrame()
    save_p = False  # save data as pickle file
    load_p = False  # load data as pickle file
    save_csv = False  # save data as csv file
    # pickle file for saving data
    file_p = 'data.p'
    # csv file for saving data
    file_data_csv = 'data.csv'

    def __init__(self,
                 files_reports: list,
                 save_p: bool,
                 load_p: bool,
                 save_csv: bool):
        # list of files with raw data
        self.files_reports = files_reports
        # save data as pickle file
        self.save_p = save_p
        # load data as pickle file
        self.load_p = load_p
        # save data as csv file
        self.save_csv = save_csv

    def read_data(self, filter_data=True, clean_data=True):
        """Read data into an attribute.

        Args:
            filter_data (bool, optional): flag for filtering data.
            clean_data (bool, optional): clean data.

        Returns:
            dataframe: updated dataframe.
        """
        # load data
        if self.load_p:
            df = gpte.common.load_from_p(self.file_p, 'chatgpt data')
        # get data based on the reports
        else:
            # pandas df to store data
            df = pd.DataFrame()
            # df = df.transpose()
            # go over all reports
            for file in tqdm(os.listdir(self.files_reports)):
                file = os.fsdecode(file)
                logger.info('Processing report {}.', file)
                file = os.path.join(self.files_reports, file)
                f = open(file, 'r')
                # TODO: add data from the report to the dataframe
                f.close()
            # report people that attempted study
            logger.info('Processed {} reports.', df.shape[0])
            # clean data
            if clean_data:
                df = self.clean_data(df)
            # filter data
            if filter_data:
                df = self.filter_data(df)
            # sort columns alphabetically
            df = df.reindex(sorted(df.columns), axis=1)
        # save to pickle
        if self.save_p:
            gpte.common.save_to_p(self.file_p, df, 'chatgpt data')
        # save to csv
        if self.save_csv:
            df.to_csv(os.path.join(gpte.settings.output_dir, self.file_data_csv),
                      index=False)
            logger.info('Saved data to csv file {}',
                        self.file_data_csv + '.csv')
        # update attribute
        self.data = df
        # return df with data
        return df

    def filter_data(self, df):
        """
        Filter data.
        Args:
            df (dataframe): dataframe with data.

        Returns:
            dataframe: updated dataframe.
        """
        logger.error('Filtering data not implemented.')
        # assign to attribute
        self.appen_data = df
        # return df with data
        return df

    def clean_data(self, df):
        """Clean data from unexpected values.

        Args:
            df (dataframe): dataframe with data.

        Returns:
            dataframe: updated dataframe.
        """
        logger.error('Cleaning data not implemented.')
        # assign to attribute
        self.appen_data = df
        # return df with data
        return df

    def show_info(self):
        """
        Output info for data in object.
        """
        logger.info('No info to show.')
