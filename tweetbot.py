#!/usr/bin/python
# -*- coding: utf-8 -*-
# Tested at Tweetbot for Mac v2.3.4

__license__ = "WTFPL"
__author__ = "Haze Park"
__email__ = "realignist@gmail.com"

import webbrowser
import urllib

def moveto_timeline(query = ""):
    open_scheme(create_tweetbot_url("timeline"))

def moveto_mentions(query = ""):
    open_scheme(create_tweetbot_url("mentions"))

def moveto_messages(query = ""):
    open_scheme(create_tweetbot_url("direct_messages"))

def moveto_favorites(query = ""):
    open_scheme(create_tweetbot_url("favorites"))

def moveto_lists(query = ""):
    open_scheme(create_tweetbot_url("lists"))

def moveto_user_profile(query = ""):
    open_scheme(create_tweetbot_url("user_profile/" + query))

def post_tweet(query = ""):
    open_scheme(create_tweetbot_url("post?text=" + encode_query(query)))

def search_tweet(query = ""):
    open_scheme(create_tweetbot_url("search?query=" + encode_query(query)))

def moveto_mute(query = ""):
    open_scheme(create_tweetbot_url("mute/keyword"))

def encode_query(query = ""):
    return urllib.quote_plus(query)

def create_tweetbot_url(string):
    return "tweetbot:///" + string

def open_scheme(uri):
    webbrowser.open(uri)