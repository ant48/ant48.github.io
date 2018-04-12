import main_display
import media

# movie input
parent_trap = media.Movie("Parent Trap", "1hr 45mins",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/Parenttrapposter.jpg",
                          "https://www.youtube.com/watch?v=32WeiH4TrIY",
                          "Identical twins Annie and Hallie, discover each "
                          "other for the first time at summer camp and make a "
                          "plan to bring their wayward parents back together.",
                          "1998")

avatar = media.Movie("Avatar", "2hr 50mins",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "A paraplegic marine dispatched to the moon Pandora on a"
                     " unique mission becomes torn between following his"
                     " orders and protecting the world he feels is his home.",
                     "2009")

kong_skull = media.Movie("Kong: Skull Island", "2hr 53mins",
                         "https://upload.wikimedia.org/wikipedia/en/3/34/Kong_Skull_Island_poster.jpg",
                         "https://www.youtube.com/watch?v=44LdLqgOpjo",
                         "A team of scientists explore an uncharted island in "
                         "the Pacific, venturing into the domain of the mighty"
                         " Kong, and must fight to escape a primal Eden.",
                         "2017")

power_rangers = media.Movie("Power Rangers", "2hr 13mins",
                            "https://upload.wikimedia.org/wikipedia/en/7/78/Power_Rangers_%282017_Official_Theatrical_Poster%29.png",
                            "https://www.youtube.com/watch?v=5kIe6UZHSXw",
                            "A group of high-school students, who are infused "
                            "with unique superpowers, harness their abilities "
                            "in order to save the world before it is controlled"
                            " by the enemy.", "2017")


# tv shows input
bones = media.TV_Shows("Bones", "12 seasons",
                       "https://upload.wikimedia.org/wikipedia/en/3/39/Bones_title_card.png",
                       "https://www.youtube.com/watch?v=luL1BaK87mA",
                       "246 episodes", "Fox")

fresh = media.TV_Shows("Fresh Off The Boat", "3 seasons",
                      "https://upload.wikimedia.org/wikipedia/en/1/11/Fresh_Off_the_Boat_intertitle.png",
                      "https://www.youtube.com/watch?v=1KhRKkLS_4I",
                      "60 episodes", "ABC")

dessert = media.TV_Shows("Top Chef: Just Desserts", "2 seasons",
                         "https://upload.wikimedia.org/wikipedia/en/5/5e/Top_Chef_Just_Desserts_logo.png",
                         "https://www.youtube.com/watch?v=lJ_DpIWpH6M",
                         "20 episodes", "Bravo")


# add all movies and shows in list
movies = [avatar, kong_skull, parent_trap, power_rangers]
shows = [bones, dessert, fresh]

main_display.open_video_page(movies, shows)
