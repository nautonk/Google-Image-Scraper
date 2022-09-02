# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    #Release resources
    del image_scraper

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(set(["Literacy Book", "National Literacy Day", "Quotes On Literacy", "Literacy Posters", "Reading Day", "Literacy Slogans", "Tolkien Day", "World Reading Day", "Literacy Week Ideas", "Literacy Background", "Literacy Banner", "Happy Literacy Day", "Literacy Word Art", "Literacy Day Activities", "September Special Days", "Happy Book Day", "International Literacy Day Clip Art", "International Day of éducation", "Literacy Night Clip Art", "Computer Literacy Day", "Indigenous Language", "Reading Festival", "Roald Dahl Day", "Family Literacy Activities", "Storytelling", "Cien Anos De Soledad", "Literacy Cover Page", "Literacy Development", "Neuromythe", "National Literacy Month", "Financial Literacy Month", "Special Day Quotes", "Quotes About Literacy", "Special Days of the Year", "Literacy Fair", "Littaracy", "International Book Day", "Images of Digital Literacy", "International Literacy Day Logo", "September 8 Day", "Family Literacy Night Flyer", "International Peace Day", "Adult Illiteracy", "Dr. Seuss Day", "Happy International Kids Day", "Literacy Games and Activities", "International Day of Education", "Digital Learning Day Craft", "Celebrate Literacy", "Digitally Literate"]))

    #Parameters
    number_of_images = 50                # Desired number of images
    headless = True                     # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (9999, 9999)       # Maximum desired image resolution
    max_missed = 1000                   # Max number of failed images before exit
    number_of_workers = 2               # Number of "workers" used
    keep_filenames = True              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
