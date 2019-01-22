""" Module to manage affiliate marketing links

Purpose: allow managing affiliate marketing links in one place
Author: Tom W. Hartung
Date: Winter, 2019
Copyright: (c) 2019 Tom W. Hartung, Groja.com, and JooMoo Websites LLC.
Reference:

"""


class AffiliateLinks:

    """
    Use python dictionaries to make it easier to update affiliate links
    """

    #
    # Source Link Dictionaries:
    #
    afl_none = {
        'what_is_man': '',
        'mt_by_burns': '',
        'flw_by_burns': '',
        'deep_work': '',
        'ah_by_chernow': '',
        'bf_by_isaacson': '',
        'gw_by_chernow': '',
        'ja_by_mccullough': '',
        'ja_by_hbo': '',
        'ph_by_kukla': '',
        'tj_himself': '',
        'tj_by_burns': '',
        'xxx': '',
    }

    #
    # Active Link Dictionaries:
    #
    afl_content = {}
    afl_button = {}

    def __init__(self):

        """
        Assign source links to active links
        """

        #
        # About page
        #
        self.afl_content['what_is_man'] = afl_none['what_is_man']

        #
        # Opinions list page
        #
        self.afl_content['mt_by_burns'] = afl_none['mt_by_burns']
        self.afl_content['flw_by_burns'] = afl_none['flw_by_burns']

        #
        # Deep Work article
        #
        self.afl_content['deep_work'] = afl_none['deep_work']
        self.afl_content['deep_work'] = afl_none['deep_work']

        #
        # Hamilton and Jefferson article
        #
        self.afl_content['ah_by_chernow'] = afl_none['ah_by_chernow']
        self.afl_button['ah_by_chernow'] = afl_none['ah_by_chernow']

        self.afl_content['bf_by_isaacson'] = afl_none['bf_by_isaacson']
        self.afl_button['bf_by_isaacson'] = afl_none['bf_by_isaacson']

        self.afl_content['gw_by_chernow'] = afl_none['gw_by_chernow']
        self.afl_button['gw_by_chernow'] = afl_none['gw_by_chernow']

        self.afl_content['ja_by_mccullough'] = afl_none['ja_by_mccullough']
        self.afl_button['ja_by_mccullough'] = afl_none['ja_by_mccullough']
        self.afl_content['ja_by_hbo'] = afl_none['ja_by_hbo']
        self.afl_button['ja_by_hbo'] = afl_none['ja_by_hbo']

        self.afl_content['ph_by_kukla'] = afl_none['ph_by_kukla']
        self.afl_button['ph_by_kukla'] = afl_none['ph_by_kukla']

        self.afl_content['tj_himself'] = afl_none['tj_himself']
        self.afl_button['tj_himself'] = afl_none['tj_himself']
        self.afl_content['tj_by_burns'] = afl_none['tj_by_burns']
        self.afl_button['tj_by_burns'] = afl_none['tj_by_burns']

        self.afl_content['xxx'] = afl_none['xxx']
        self.afl_button['xxx'] = afl_none['xxx']
