import csv

userMovie = input("What movie are you watching: ")
movieFound = False

with open('netflix_.csv', 'r', newline='') as csvfile:
    movieList = csv.reader(csvfile, delimiter=',')
    
    for title in movieList:
        if userMovie in title:
            movieFound = True
            break
        
if movieFound:
    print(f"{title[-7]} is rated {title[-6]} with a rating {title[-2]} ")
else:
    print("Movie not found")