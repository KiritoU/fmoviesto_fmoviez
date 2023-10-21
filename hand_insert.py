from fmoviez import FmovieZ

############## Mau cho Movie
# film_data = {
#     "title": "Fog City",
#     "slug": "fog-city",
#     "description": "A mysterious fog forces a group of friends to take cover before it's too late. Once trapped inside, they'll soon find out it's already too late.",
#     "post_type": "single",
#     "trailer_id": "embed",
#     "cover_src": "https://web.fmoviesto.site/_sf/288/25283717.jpg",
#     "extra_info": {
#         "Quality": "HD",
#         "IMDb": "5.7",
#         "Duration": "90 min",
#         "Country": " United States",
#         "Genre": "Movies, Horror, Thriller",
#         "Released": "2023",
#         "Director": "Steve Wolsh",
#         "Casts": " Jonny Beauchamp, Luke Benward, Brianne Cordaro",
#         "Tags": "Watch Fog City Online Free,Fog City Online Free,Where to watch Fog City,Fog City movie free online,Fog City free online",
#     },
# }
# episodes_data = {"Episode 1": "https://vidsrc.to/embed/movie/tt5105136"}


############## Mau cho TV Shows
film_data = {
    "title": "LEGO Masters Season 4",
    "slug": "lego-masters-season-4",
    "description": "Teams of LEGO enthusiasts go head-to-head, with infinite possibilities and an unlimited supply of LEGO bricks. Teams of two will compete against each other in ambitious brick-building challenges to be crowned the country's most talented amateur LEGO builders. Based on the hit British reality-competition series of the same name.",
    "post_type": "series",
    "trailer_id": "Tca9lWVUJGw",
    "cover_src": "https://web.fmoviesto.site/_sf/288/65087010.jpg",
    "extra_info": {
        "Quality": "HD",
        "IMDb": "7.5",
        "Duration": "45 min",
        "Country": " United States",
        "Genre": "TV Shows",
        "Released": "2023",
        "Director": "-",
        "Casts": " Will Arnett, Jamie Berard, Amy Corbett",
        "Tags": "Watch LEGO Masters Season 4 Online Free,LEGO Masters Season 4 Online Free,Where to watch LEGO Masters Season 4,LEGO Masters Season 4 movie free online,LEGO Masters Season 4 free online",
    },
}
episodes_data = {
    "Episode 1": "https://vidsrc.to/embed/tv/tt9615014/4/1",
    "Episode 2": "https://vidsrc.to/embed/tv/tt9615014/4/2",
    "Episode 3": "https://vidsrc.to/embed/tv/tt9615014/4/3",
    "Episode 4": "https://vidsrc.to/embed/tv/tt9615014/4/4",
}


def main():
    FmovieZ(film=film_data, episodes=episodes_data).insert_film()


if __name__ == "__main__":
    main()
