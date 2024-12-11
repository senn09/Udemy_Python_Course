import spotifyManager
import billboardScraper

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
scraper = billboardScraper.BillboardScraper(date)
track_list = scraper.getTrackList()
spotipyManager = spotifyManager.SpotifyManager(track_list=track_list, date=date)



