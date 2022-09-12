# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, image_path, search_key, extra_search_params, number_of_images, headless, min_resolution,
        max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    # Release resources
    del image_scraper


if __name__ == "__main__":
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    # Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(
        set(["Origami Paper Art", "Origami Cube", "Origami Bookmark", "Origami Step by Step", "Origami Dragon",
             "Easy Origami", "Origami Fox", "Origami Dress", "DIY Origami", "Origami Print", "Origami Decorations",
             "Origami Tools", "Origami Crafts", "Origami Letters", "Funny Origami", "Kirigami Origami",
             "Japanese Origami", "Origami with Money", "Advanced Origami", "Origami Art", "Origami Kusudama",
             "Origami Objects", "Origami Decor", "Modular Origami", "Origami Club", "Origami Shapes",
             "Cool Origami Ideas", "Origami Human", "Beautiful Origami", "Origami Star", "Origami Boxes",
             "Origami World", "Japanese Origami Paper", "Modern Origami", "Japan Origami", "Origami Projects",
             "Beginner Origami", "Origami Ninja", "Origami Baby", "Origami Butterflies", "Origami Angel",
             "Origami Dove", "Origami Drawing", "Origami Love", "Fabric Origami", "Origami People", "Origami Artist",
             "Origami Cat", "Origami Boxes Easy", "Origami Yoda", "Origami Gift Box", "Origami Tessellation",
             "Origami Bug", "Origami Bracelet", "Unit Origami", "Origami Jewelry", "Fun Origami", "Origami Goldfish",
             "Origami Chair", "Origami Sheets", "Traditional Origami", "Origami Furniture", "Origami Frog",
             "Origami Paper Lanterns", "Origami Umbrella", "Difficult Origami", "Geometric Origami", "Origami Anime",
             "Origami Magic", "Origami Book"]))

    # Parameters
    number_of_images = 200  # Desired number of images
    headless = True  # True = No Chrome GUI
    min_resolution = (1000, 1500)  # Minimum desired image resolution
    max_resolution = (9999, 9999)  # Maximum desired image resolution
    max_missed = 1000  # Max number of failed images before exit
    number_of_workers = 2  # Number of "workers" used
    keep_filenames = True  # Keep original URL image filenames
    extra_search_params = '-inurl:freepik.com'
    number_of_workers = 1  # Number of "workers" used
    keep_filenames = False  # Keep original URL image filenames

    # Run each search_key in a separate thread
    # Automatically waits for all threads to finish
    # Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
